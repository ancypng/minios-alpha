"""Simulated file system for MiniOS Alpha.

Files and directories live in a tree of Python dictionaries. The tree is saved
to minios_disk.json so files survive between runs. Nothing touches the real disk
except that one JSON file.
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
        self.cwd = []  # list of directory names from the root
        self._load()

    # ---------- persistence ----------
    def _load(self):
        try:
            with open(self.disk_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            if data.get("type") == "dir":
                self.root = data
        except (OSError, ValueError):
            self.root = _new_dir()

    def _save(self):
        try:
            with open(self.disk_file, "w", encoding="utf-8") as f:
                json.dump(self.root, f, indent=2)
        except OSError:
            pass  # saving is a convenience; never crash the shell

    # ---------- path helpers ----------
    def _parts(self, path):
        if path.startswith(("/", "\\")):
            parts = []
        else:
            parts = list(self.cwd)
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
        node = self.root
        for name in parts:
            if node["type"] != "dir" or name not in node["children"]:
                raise FileSystemError("Path does not exist.")
            node = node["children"][name]
        return node

    def _parent_and_name(self, path):
        parts = self._parts(path)
        if not parts:
            raise FileSystemError("Invalid name.")
        parent = self._node(parts[:-1])
        if parent["type"] != "dir":
            raise FileSystemError("Path does not exist.")
        return parent, parts[-1]

    @staticmethod
    def _check_name(name):
        if not name or any(c in INVALID_CHARS for c in name):
            raise FileSystemError('Invalid name. Avoid / \\ : * ? " < > |')

    def pwd(self):
        return "\\" + "\\".join(self.cwd)

    # ---------- commands ----------
    def listdir(self, path="."):
        node = self._node(self._parts(path))
        if node["type"] != "dir":
            raise FileSystemError("Not a directory.")
        rows = []
        for name in sorted(node["children"], key=str.lower):
            child = node["children"][name]
            if child["type"] == "dir":
                rows.append(f"{'<DIR>':>10}  {name}")
            else:
                rows.append(f"{len(child['content']):>10}  {name}")
        return rows

    def mkdir(self, path):
        parent, name = self._parent_and_name(path)
        self._check_name(name)
        if name in parent["children"]:
            raise FileSystemError("A file or directory with that name already exists.")
        parent["children"][name] = _new_dir()
        self._save()

    def create(self, path):
        parent, name = self._parent_and_name(path)
        self._check_name(name)
        if name in parent["children"]:
            raise FileSystemError("A file or directory with that name already exists.")
        parent["children"][name] = {"type": "file", "content": ""}
        self._save()

    def read(self, path):
        parts = self._parts(path)
        try:
            node = self._node(parts)
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
        files = dirs = 0
        stack = [self.root]
        while stack:
            node = stack.pop()
            for child in node["children"].values():
                if child["type"] == "dir":
                    dirs += 1
                    stack.append(child)
                else:
                    files += 1
        return files, dirs
