import os
import platform
import sys
import time
from datetime import datetime

from filesystem import FileSystem, FileSystemError
from memory import MemoryError_, MemoryManager
from processes import ProcessError, ProcessManager
from users import UserManager

OS_NAME = "MiniOS Alpha"
VERSION = "1.0"
LINE = "=" * 40

HELP = [
    (
        "General",
        [
            ("help", "Show this list"),
            ("clear", "Clear the screen"),
            ("date / time", "Show the date / the time"),
            ("whoami", "Show the current user"),
            ("systeminfo", "Show system information"),
            ("history", "Show commands typed this session"),
            ("echo <text>", "Print text"),
            ("version", "Show the MiniOS version"),
            ("exit", "Shut down MiniOS"),
        ],
    ),
    (
        "Files",
        [
            ("dir [path]", "List files and folders"),
            ("mkdir <name>", "Create a directory"),
            ("create <file>", "Create an empty file"),
            ("write <file> <text>", "Write text into a file"),
            ("read <file>", "Show a file's contents"),
            ("delete <name>", "Delete a file or empty directory"),
            ("rename <old> <new>", "Rename a file or directory"),
            ("cd <path>", "Change directory (cd .. goes up)"),
            ("pwd", "Show the current directory"),
        ],
    ),
    (
        "Processes",
        [
            ("run <name>", "Start a simulated process"),
            ("process", "List running processes"),
            ("kill <pid>", "Terminate a process"),
        ],
    ),
    (
        "Memory",
        [
            ("memory", "Show memory status"),
            ("allocate <MB>", "Allocate memory"),
            ("free <MB>", "Release memory"),
        ],
    ),
    (
        "Users",
        [
            ("users", "List user accounts"),
            ("logout", "Log out and return to login"),
            ("login", "Switch user (alias of logout)"),
        ],
    ),
]


class MiniOS:
    def __init__(self):
        self.fs = FileSystem()
        self.procs = ProcessManager()
        self.mem = MemoryManager()
        self.users = UserManager()
        self.history = []
        self.boot_time = time.time()
        self.running = True
        self.commands = {
            "help": self.cmd_help,
            "clear": self.cmd_clear,
            "cls": self.cmd_clear,
            "date": self.cmd_date,
            "time": self.cmd_time,
            "whoami": self.cmd_whoami,
            "systeminfo": self.cmd_systeminfo,
            "history": self.cmd_history,
            "echo": self.cmd_echo,
            "version": self.cmd_version,
            "exit": self.cmd_exit,
            "shutdown": self.cmd_exit,
            "dir": self.cmd_dir,
            "ls": self.cmd_dir,
            "mkdir": self.cmd_mkdir,
            "create": self.cmd_create,
            "write": self.cmd_write,
            "read": self.cmd_read,
            "delete": self.cmd_delete,
            "rename": self.cmd_rename,
            "cd": self.cmd_cd,
            "pwd": self.cmd_pwd,
            "process": self.cmd_process,
            "run": self.cmd_run,
            "kill": self.cmd_kill,
            "memory": self.cmd_memory,
            "allocate": self.cmd_allocate,
            "free": self.cmd_free,
            "users": self.cmd_users,
            "logout": self.cmd_logout,
            "login": self.cmd_logout,
        }

    # startup or lop
    def banner(self):
        print(LINE)
        print(f"{'MINI OS ALPHA v' + VERSION:^40}")
        print(LINE)
        print("\nWelcome to MiniOS!\n")

    def login_screen(self):
        print(LINE)
        print(f"{'MiniOS Login':^40}")
        print(LINE)
        print("Demo accounts: admin / admin123, student / student123\n")
        return self.users.login_prompt()

    def start(self):
        self.banner()
        try:
            while self.running:
                if not self.users.current:
                    if not self.login_screen():
                        print("Too many failed attempts. Shutting down MiniOS...")
                        return
                    print("Type 'help' to see the available commands.\n")
                self.shell_loop()
        except (EOFError, KeyboardInterrupt):
            print("\n\nShutting down MiniOS...\n\nGoodbye!")

    def shell_loop(self):
        while self.running and self.users.current:
            line = input("MiniOS> ").strip()
            if not line:
                continue
            self.history.append(line)
            self.execute(line)
            print()

    def execute(self, line):
        parts = line.split()
        name, args = parts[0].lower(), parts[1:]
        handler = self.commands.get(name)
        if handler is None:
            print("Unknown command.\n\nType 'help' to see the available commands.")
            return
        try:
            handler(args, line)
        except FileSystemError as e:
            print(f"Error: {e}")
        except ProcessError as e:
            print(f"Error: {e}")
        except MemoryError_ as e:
            print(f"Error: {e}")
        except Exception as e:  # last-resort safety net: never crash the shell
            print(f"Error: Something went wrong ({type(e).__name__}).")

    # Helper
    @staticmethod
    def need(args, n, usage):
        if len(args) < n:
            raise FileSystemError(f"Missing argument. Usage: {usage}")

    @staticmethod
    def to_int(text, what):
        try:
            return int(text)
        except ValueError:
            raise MemoryError_(f"{what} must be a whole number.")

    # Basta General
    def cmd_help(self, args, line):
        print("Available Commands:")
        for section, items in HELP:
            print(f"\n[{section}]")
            for cmd, desc in items:
                print(f"  {cmd:<22}{desc}")

    def cmd_clear(self, args, line):
        os.system("cls" if os.name == "nt" else "clear")

    def cmd_date(self, args, line):
        print(datetime.now().strftime("Current Date: %A, %B %d, %Y"))

    def cmd_time(self, args, line):
        print(datetime.now().strftime("Current Time: %I:%M:%S %p"))

    def cmd_whoami(self, args, line):
        print(f"Current User: {self.users.current}")

    def cmd_history(self, args, line):
        for i, c in enumerate(self.history, 1):
            print(f"{i:>3}  {c}")

    def cmd_echo(self, args, line):
        print(" ".join(args))

    def cmd_version(self, args, line):
        print(f"{OS_NAME} v{VERSION}")

    def cmd_exit(self, args, line):
        print("Shutting down MiniOS...\n\nGoodbye!")
        self.running = False

    def cmd_systeminfo(self, args, line):
        files, dirs = self.fs.counts()
        uptime = int(time.time() - self.boot_time)
        print(LINE)
        print(f"{'SYSTEM INFORMATION':^40}")
        print(LINE)
        print()
        print(f"OS Name:      {OS_NAME}")
        print(f"Version:      {VERSION}")
        print(f"Architecture: {'64-bit' if sys.maxsize > 2**32 else '32-bit'}")
        print("CPU:          Virtual CPU")
        print(f"Memory:       {self.mem.TOTAL_MB} MB ({self.mem.used} MB used)")
        print(f"Host:         {platform.system()} (Python {platform.python_version()})")
        print(f"User:         {self.users.current} ({self.users.role()})")
        print(f"Processes:    {self.procs.count()} running")
        print(f"Files/Dirs:   {files} file(s), {dirs} folder(s)")
        print(f"Uptime:       {uptime // 60}m {uptime % 60}s")
        print()
        print(LINE)

    # ---------- files ----------
    def cmd_dir(self, args, line):
        path = args[0] if args else "."
        rows = self.fs.listdir(path)
        print(f"Directory of {self.fs.pwd() if path == '.' else path}\n")
        print("\n".join(rows) if rows else "  (empty)")

    def cmd_mkdir(self, args, line):
        self.need(args, 1, "mkdir <folder>")
        self.fs.mkdir(args[0])
        print("Directory created.")

    def cmd_create(self, args, line):
        self.need(args, 1, "create <file>")
        self.fs.create(args[0])
        print("File created.")

    def cmd_write(self, args, line):
        self.need(args, 2, "write <file> <text>")
        text = line.split(None, 2)[2]
        self.fs.write(args[0], text)
        print("File saved.")

    def cmd_read(self, args, line):
        self.need(args, 1, "read <file>")
        content = self.fs.read(args[0])
        print(content if content else "(file is empty)")

    def cmd_delete(self, args, line):
        self.need(args, 1, "delete <name>")
        kind = self.fs.delete(args[0])
        print("Directory deleted." if kind == "dir" else "File deleted.")

    def cmd_rename(self, args, line):
        self.need(args, 2, "rename <old> <new>")
        self.fs.rename(args[0], args[1])
        print("Renamed.")

    def cmd_cd(self, args, line):
        self.fs.cd(args[0] if args else "\\")
        print(f"Current directory: {self.fs.pwd()}")

    def cmd_pwd(self, args, line):
        print(self.fs.pwd())

    # ---------- processes ----------
    def cmd_run(self, args, line):
        self.need(args, 1, "run <name>")
        p = self.procs.run(args[0])
        print("Process started.\n")
        print(f"PID: {p['pid']}")
        print(f"Name: {p['name']}")
        print(f"Status: {p['status']}")

    def cmd_process(self, args, line):
        procs = self.procs.list()
        if not procs:
            print("No running processes.")
            return
        print(f"{'PID':<7}{'NAME':<16}{'STATUS':<10}STARTED")
        for p in procs:
            print(f"{p['pid']:<7}{p['name']:<16}{p['status']:<10}{p['started']}")

    def cmd_kill(self, args, line):
        self.need(args, 1, "kill <pid>")
        try:
            pid = int(args[0])
        except ValueError:
            raise ProcessError("PID must be a whole number.")
        self.procs.kill(pid)
        print(f"Process {pid} terminated.")

    # ---------- memory ----------
    def cmd_memory(self, args, line):
        print("\n".join(self.mem.status_lines()))

    def cmd_allocate(self, args, line):
        self.need(args, 1, "allocate <MB>")
        mb = self.to_int(args[0], "Amount")
        self.mem.allocate(mb)
        print(f"{mb} MB allocated.")

    def cmd_free(self, args, line):
        self.need(args, 1, "free <MB>")
        mb = self.to_int(args[0], "Amount")
        self.mem.release(mb)
        print(f"{mb} MB released.")

    # ---------- users ----------
    def cmd_users(self, args, line):
        print(f"{'USER':<12}ROLE")
        for name, role in self.users.list_users():
            marker = "  <- you" if name == self.users.current else ""
            print(f"{name:<12}{role}{marker}")

    def cmd_logout(self, args, line):
        print(f"Logging out {self.users.current}...\n")
        self.users.logout()


if __name__ == "__main__":
    MiniOS().start()
