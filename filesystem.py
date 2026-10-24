"""Simulated file system for MiniOS Alpha.

Files and directories live in a tree of Python dictionaries:

    directory -> {"type": "dir",  "children": {name: node, ...}}
    file      -> {"type": "file", "content": "text"}

The tree is saved to minios_disk.json so files survive between runs.
Nothing touches the real disk except that one JSON file.
"""
import json
import os

INVALID_CHARS = set('/\\:*?"<>|')
DISK_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "minios_disk.json")


class FileSystemError(Exception):
    """Raised for any user-facing file system problem."""


def _new_dir():
    return {"type": "dir", "children": {}}


class FileSystem:
    def __init__(self, disk_file=DISK_FILE):
        self.disk_file = disk_file
        self.root = _new_dir()
        self.cwd = []  # names of the folders from the root to the current folder
        self._load()

    # ------------------------------------------------------------
    # Saving and loading
    # ------------------------------------------------------------
    def _load(self):
        try:
            with open(self.disk_file, "r", encoding="utf-8") as file:
                data = json.load(file)
            if data.get("type") == "dir":
                self.root = data
        except (OSError, ValueError):
            self.root = _new_dir()  # missing or damaged disk -> start empty

    def _save(self):
        try:
            with open(self.disk_file, "w", encoding="utf-8") as file:
                json.dump(self.root, file, indent=2)
        except OSError:
            pass  # saving is a convenience; never crash the shell

    # ------------------------------------------------------------
    # Path helpers
    # ------------------------------------------------------------
    def _parts(self, path):
        """Turn a path like '..\\docs/a.txt' into a list of names."""
        starts_at_root = path.startswith(("/", "\\"))
        parts = [] if starts_at_root else list(self.cwd)
        for piece in path.replace("\\", "/").split("/"):
            if piece in ("", "."):
                continue
            if piece == "..":
                if parts:
                    parts.pop()
            else:
                parts.append(piece)
        return parts

    def _node(self, parts):
        """Follow a list of names down the tree and return that node."""
        node = self.root
        for name in parts:
            if node["type"] != "dir" or name not in node["children"]:
                raise FileSystemError("Path does not exist.")
            node = node["children"][name]
        return node

    def _parent_and_name(self, path):
        """Return (parent directory node, last name) for a path."""
        parts = self._parts(path)
        if not parts:
            raise FileSystemError("Invalid name.")
        parent = self._node(parts[:-1])
        if parent["type"] != "dir":
            raise FileSystemError("Path does not exist.")
        return parent, parts[-1]

    @staticmethod
    def _check_name(name):
        if not name or any(char in INVALID_CHARS for char in name):
            raise FileSystemError('Invalid name. Avoid / \\ : * ? " < > |')

    def _add_node(self, path, node):
        """Create a new file/folder, refusing duplicate names."""
        parent, name = self._parent_and_name(path)
        self._check_name(name)
        if name in parent["children"]:
            raise FileSystemError("A file or directory with that name already exists.")
        parent["children"][name] = node
        self._save()

    def pwd(self):
        """Current directory as text, e.g. \\Documents\\School"""
        return "\\" + "\\".join(self.cwd)

    # ------------------------------------------------------------
    # Commands
    # ------------------------------------------------------------
    def listdir(self, path="."):
        """Return a list of (name, is_directory, size) for a folder."""
        node = self._node(self._parts(path))
        if node["type"] != "dir":
            raise FileSystemError("Not a directory.")
        items = []
        for name in sorted(node["children"], key=str.lower):
            child = node["children"][name]
            if child["type"] == "dir":
                items.append((name, True, 0))
            else:
                items.append((name, False, len(child["content"])))
        return items

    def mkdir(self, path):
        self._add_node(path, _new_dir())

    def create(self, path):
        self._add_node(path, {"type": "file", "content": ""})

    def read(self, path):
        try:
            node = self._node(self._parts(path))
        except FileSystemError:
            raise FileSystemError("File does not exist.")
        if node["type"] != "file":
            raise FileSystemError("That is a directory, not a file.")
        return node["content"]

    def write(self, path, text):
        parent, name = self._parent_and_name(path)
        self._check_name(name)
        existing = parent["children"].get(name)
        if existing and existing["type"] == "dir":
            raise FileSystemError("That is a directory, not a file.")
        parent["children"][name] = {"type": "file", "content": text}
        self._save()

    def delete(self, path):
        """Delete a file or an empty directory. Returns 'file' or 'dir'."""
        parent, name = self._parent_and_name(path)
        node = parent["children"].get(name)
        if node is None:
            raise FileSystemError("File or directory does not exist.")
        if node["type"] == "dir" and node["children"]:
            raise FileSystemError("Directory is not empty.")
        del parent["children"][name]
        self._save()
        return node["type"]

    def rename(self, old, new):
        parent, old_name = self._parent_and_name(old)
        if old_name not in parent["children"]:
            raise FileSystemError("File or directory does not exist.")
        self._check_name(new)
        if new in parent["children"]:
            raise FileSystemError("A file or directory with that name already exists.")
        parent["children"][new] = parent["children"].pop(old_name)
        self._save()

    def cd(self, path):
        parts = self._parts(path)
        try:
            node = self._node(parts)
        except FileSystemError:
            raise FileSystemError("Directory does not exist.")
        if node["type"] != "dir":
            raise FileSystemError("That is a file, not a directory.")
        self.cwd = parts

    def counts(self):
        """Return (number of files, number of directories) in the whole disk."""
        files = dirs = 0
        to_visit = [self.root]
        while to_visit:
            folder = to_visit.pop()
            for child in folder["children"].values():
                if child["type"] == "dir":
                    dirs += 1
                    to_visit.append(child)
                else:
                    files += 1
        return files, dirs
