"""MiniOS Alpha - the shell (prompt, command parsing and error handling).

Run with:  python main.py
This is only a simulation. It does not touch real Windows processes or memory.
"""
import os
import platform
import sys
import time
from datetime import datetime

from filesystem import FileSystem, FileSystemError
from memory import MemoryManager, MemoryManagerError
from processes import ProcessManager, ProcessError
from users import UserManager

OS_NAME = "MiniOS Alpha"
VERSION = "1.0"
WIDTH = 50
LINE = "=" * WIDTH
THIN_LINE = "-" * WIDTH


class UsageError(Exception):
    """Raised when a command gets missing or badly formatted arguments."""


# Errors that are the user's fault: show the message, keep running.
USER_ERRORS = (FileSystemError, ProcessError, MemoryManagerError, UsageError)

# (section name, [(command, description), ...]) - used by the help command
HELP = [
    ("General", [
        ("help", "Show this list"),
        ("clear", "Clear the screen"),
        ("date / time", "Show the date / the time"),
        ("whoami", "Show the current user"),
        ("systeminfo", "Show system information"),
        ("history", "Show commands typed this session"),
        ("echo <text>", "Print text"),
        ("version", "Show the MiniOS version"),
        ("exit", "Shut down MiniOS"),
    ]),
    ("Files", [
        ("dir [path]", "List files and folders"),
        ("mkdir <name>", "Create a directory"),
        ("create <file>", "Create an empty file"),
        ("write <file> <text>", "Write text into a file"),
        ("read <file>", "Show a file's contents"),
        ("delete <name>", "Delete a file or empty directory"),
        ("rename <old> <new>", "Rename a file or directory"),
        ("cd <path>", "Change directory (cd .. goes up)"),
        ("pwd", "Show the current directory"),
    ]),
    ("Processes", [
        ("run <name>", "Start a simulated process"),
        ("process", "List running processes"),
        ("kill <pid>", "Terminate a process"),
    ]),
    ("Memory", [
        ("memory", "Show memory status"),
        ("allocate <MB>", "Allocate memory"),
        ("free <MB>", "Release memory"),
    ]),
    ("Users", [
        ("users", "List user accounts"),
        ("logout", "Log out and return to login"),
        ("login", "Switch user (same as logout)"),
    ]),
]


# ----------------------------------------------------------------
# Small printing helpers (keep all output looking the same)
# ----------------------------------------------------------------
def print_title(text):
    print(LINE)
    print(text.center(WIDTH))
    print(LINE)


def print_ok(message):
    print(f"[OK] {message}")


def print_error(message):
    print(f"[ERROR] {message}")


def print_row(label, value, label_width=14):
    print(f"{label + ':':<{label_width}}{value}")


class MiniOS:
    def __init__(self):
        self.fs = FileSystem()
        self.procs = ProcessManager()
        self.mem = MemoryManager()
        self.users = UserManager()
        self.history = []
        self.boot_time = time.time()
        self.running = True

        # command word -> method that handles it
        self.commands = {
            # general
            "help": self.cmd_help, "clear": self.cmd_clear, "cls": self.cmd_clear,
            "date": self.cmd_date, "time": self.cmd_time, "whoami": self.cmd_whoami,
            "systeminfo": self.cmd_systeminfo, "history": self.cmd_history,
            "echo": self.cmd_echo, "version": self.cmd_version,
            "exit": self.cmd_exit, "shutdown": self.cmd_exit,
            # files
            "dir": self.cmd_dir, "ls": self.cmd_dir, "mkdir": self.cmd_mkdir,
            "create": self.cmd_create, "write": self.cmd_write, "read": self.cmd_read,
            "delete": self.cmd_delete, "rename": self.cmd_rename,
            "cd": self.cmd_cd, "pwd": self.cmd_pwd,
            # processes
            "process": self.cmd_process, "run": self.cmd_run, "kill": self.cmd_kill,
            # memory
            "memory": self.cmd_memory, "allocate": self.cmd_allocate, "free": self.cmd_free,
            # users
            "users": self.cmd_users, "logout": self.cmd_logout, "login": self.cmd_logout,
        }

    # ============================================================
    # Startup and main loop
    # ============================================================
    def banner(self):
        print(LINE)
        print(f"MINIOS ALPHA v{VERSION}".center(WIDTH))
        print("Operating Systems Final Project".center(WIDTH))
        print(LINE)
        print("\nWelcome to MiniOS!\n")
        print("Created by PE, BALICAO, MENDOZA, STP. THOMAS, TUMAYAO \n")

    def login_screen(self):
        print_title("MiniOS Login")
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
            line = input("MiniOS Alpha> ").strip()
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
            print_error(f"Unknown command '{name}'. Type 'help' to see the available commands.")
            return
        try:
            handler(args, line)
        except USER_ERRORS as error:
            print_error(error)
        except Exception as error:  # last-resort safety net: never crash the shell
            print_error(f"Something went wrong ({type(error).__name__}).")

    # ============================================================
    # Argument helpers
    # ============================================================
    @staticmethod
    def need(args, count, usage):
        """Make sure a command received enough arguments."""
        if len(args) < count:
            raise UsageError(f"Missing argument. Usage: {usage}")

    @staticmethod
    def to_int(text, what):
        """Convert text to a whole number or raise a friendly error."""
        try:
            return int(text)
        except ValueError:
            raise UsageError(f"{what} must be a whole number.")

    # ============================================================
    # General commands
    # ============================================================
    def cmd_help(self, args, line):
        print_title("AVAILABLE COMMANDS")
        for section, items in HELP:
            print(f"\n[{section}]")
            for command, description in items:
                print(f"  {command:<22}{description}")

    def cmd_clear(self, args, line):
        os.system("cls" if os.name == "nt" else "clear")

    def cmd_date(self, args, line):
        print(datetime.now().strftime("Current Date: %A, %B %d, %Y"))

    def cmd_time(self, args, line):
        print(datetime.now().strftime("Current Time: %I:%M:%S %p"))

    def cmd_whoami(self, args, line):
        print(f"Current User: {self.users.current}")

    def cmd_history(self, args, line):
        for number, command in enumerate(self.history, 1):
            print(f"{number:>3}  {command}")

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
        architecture = "64-bit" if sys.maxsize > 2**32 else "32-bit"

        print_title("SYSTEM INFORMATION")
        print()
        print_row("OS Name", OS_NAME)
        print_row("Version", VERSION)
        print_row("Architecture", architecture)
        print_row("CPU", "Virtual CPU")
        print_row("Memory", f"{self.mem.TOTAL_MB} MB ({self.mem.used} MB used)")
        print_row("Host", f"{platform.system()} (Python {platform.python_version()})")
        print_row("User", f"{self.users.current} ({self.users.role()})")
        print_row("Processes", f"{self.procs.count()} running")
        print_row("Files/Dirs", f"{files} file(s), {dirs} folder(s)")
        print_row("Uptime", f"{uptime // 60}m {uptime % 60}s")
        print()
        print(LINE)

    # ============================================================
    # File commands
    # ============================================================
    def cmd_dir(self, args, line):
        path = args[0] if args else "."
        items = self.fs.listdir(path)
        shown_path = self.fs.pwd() if path == "." else path

        print(f"Directory of {shown_path}\n")
        if not items:
            print("  (empty)")
            return
        for name, is_dir, size in items:
            size_text = "<DIR>" if is_dir else f"{size} B"
            print(f"{size_text:>10}  {name}")
        folders = sum(1 for item in items if item[1])
        print(f"\n{len(items) - folders} file(s), {folders} folder(s)")

    def cmd_mkdir(self, args, line):
        self.need(args, 1, "mkdir <folder>")
        self.fs.mkdir(args[0])
        print_ok(f"Directory '{args[0]}' created.")

    def cmd_create(self, args, line):
        self.need(args, 1, "create <file>")
        self.fs.create(args[0])
        print_ok(f"File '{args[0]}' created.")

    def cmd_write(self, args, line):
        self.need(args, 2, "write <file> <text>")
        text = line.split(None, 2)[2]  # everything after the file name
        self.fs.write(args[0], text)
        print_ok(f"File '{args[0]}' saved.")

    def cmd_read(self, args, line):
        self.need(args, 1, "read <file>")
        content = self.fs.read(args[0])
        print(content if content else "(file is empty)")

    def cmd_delete(self, args, line):
        self.need(args, 1, "delete <name>")
        kind = self.fs.delete(args[0])
        print_ok("Directory deleted." if kind == "dir" else "File deleted.")

    def cmd_rename(self, args, line):
        self.need(args, 2, "rename <old> <new>")
        self.fs.rename(args[0], args[1])
        print_ok(f"Renamed '{args[0]}' to '{args[1]}'.")

    def cmd_cd(self, args, line):
        self.fs.cd(args[0] if args else "\\")
        print(f"Current directory: {self.fs.pwd()}")

    def cmd_pwd(self, args, line):
        print(self.fs.pwd())

    # ============================================================
    # Process commands
    # ============================================================
    def cmd_run(self, args, line):
        self.need(args, 1, "run <name>")
        process = self.procs.run(args[0])
        print_ok("Process started.\n")
        print_row("PID", process["pid"], 8)
        print_row("Name", process["name"], 8)
        print_row("Status", process["status"], 8)

    def cmd_process(self, args, line):
        processes = self.procs.list()
        if not processes:
            print("No running processes.")
            return
        print(f"{'PID':<7}{'NAME':<16}{'STATUS':<10}STARTED")
        print(THIN_LINE)
        for p in processes:
            print(f"{p['pid']:<7}{p['name']:<16}{p['status']:<10}{p['started']}")
        print(f"\n{len(processes)} process(es) running")

    def cmd_kill(self, args, line):
        self.need(args, 1, "kill <pid>")
        pid = self.to_int(args[0], "PID")
        self.procs.kill(pid)
        print_ok(f"Process {pid} terminated.")

    # ============================================================
    # Memory commands
    # ============================================================
    def cmd_memory(self, args, line):
        print_title("MEMORY STATUS")
        print()
        print("\n".join(self.mem.status_lines()))

    def cmd_allocate(self, args, line):
        self.need(args, 1, "allocate <MB>")
        amount = self.to_int(args[0], "Amount")
        self.mem.allocate(amount)
        print_ok(f"{amount} MB allocated. {self.mem.free_mb} MB still free.")

    def cmd_free(self, args, line):
        self.need(args, 1, "free <MB>")
        amount = self.to_int(args[0], "Amount")
        self.mem.release(amount)
        print_ok(f"{amount} MB released. {self.mem.free_mb} MB now free.")

    # ============================================================
    # User commands
    # ============================================================
    def cmd_users(self, args, line):
        print(f"{'USER':<12}ROLE")
        print(THIN_LINE)
        for name, role in self.users.list_users():
            marker = "  <- you" if name == self.users.current else ""
            print(f"{name:<12}{role}{marker}")

    def cmd_logout(self, args, line):
        print(f"Logging out {self.users.current}...\n")
        self.users.logout()


if __name__ == "__main__":
    MiniOS().start()
