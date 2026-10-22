"""Simulated process management for MiniOS Alpha."""

from datetime import datetime


class ProcessError(Exception):
    pass


class ProcessManager:
    MAX_PROCESSES = 10

    def __init__(self):
        self._procs = {}
        self._next_pid = 1

    def run(self, name):
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
        if pid not in self._procs:
            raise ProcessError("Process does not exist.")
        return self._procs.pop(pid)

    def list(self):
        return [self._procs[p] for p in sorted(self._procs)]

    def count(self):
        return len(self._procs)
