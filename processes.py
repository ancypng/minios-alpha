"""Simulated process management for MiniOS Alpha."""
from datetime import datetime


class ProcessError(Exception):
    """Raised for any user-facing process problem."""


class ProcessManager:
    MAX_PROCESSES = 10

    def __init__(self):
        self._procs = {}    # pid -> process information
        self._next_pid = 1

    def run(self, name):
        """Start a new simulated process and return its information."""
        if len(self._procs) >= self.MAX_PROCESSES:
            raise ProcessError(
                f"Process limit reached ({self.MAX_PROCESSES}). Kill one first."
            )
        pid = self._next_pid
        self._next_pid += 1  # PIDs are never reused during a session
        self._procs[pid] = {
            "pid": pid,
            "name": name,
            "status": "RUNNING",
            "started": datetime.now().strftime("%H:%M:%S"),
        }
        return self._procs[pid]

    def kill(self, pid):
        """Terminate a process and return its information."""
        if pid not in self._procs:
            raise ProcessError(f"Process {pid} does not exist.")
        return self._procs.pop(pid)

    def list(self):
        """Return all processes, sorted by PID."""
        return [self._procs[pid] for pid in sorted(self._procs)]

    def count(self):
        return len(self._procs)
