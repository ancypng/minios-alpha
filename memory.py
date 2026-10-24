"""Simulated memory management for MiniOS Alpha."""


class MemoryManagerError(Exception):
    """Raised for any user-facing memory problem."""


class MemoryManager:
    TOTAL_MB = 1024
    OS_RESERVED_MB = 256  # memory the "kernel" always uses

    def __init__(self):
        self.allocated = 0  # memory allocated by the user with 'allocate'

    # ---------- calculated values ----------
    @property
    def used(self):
        """Total memory in use (kernel + user allocations)."""
        return self.OS_RESERVED_MB + self.allocated

    @property
    def free_mb(self):
        """Memory still available."""
        return self.TOTAL_MB - self.used

    # ---------- operations ----------
    def allocate(self, mb):
        self._check_positive(mb)
        if mb > self.free_mb:
            raise MemoryManagerError(
                f"Not enough free memory. Only {self.free_mb} MB available."
            )
        self.allocated += mb

    def release(self, mb):
        self._check_positive(mb)
        if mb > self.allocated:
            raise MemoryManagerError(
                f"Cannot free {mb} MB. Only {self.allocated} MB is allocated by you."
            )
        self.allocated -= mb

    @staticmethod
    def _check_positive(mb):
        if mb <= 0:
            raise MemoryManagerError("Amount must be a positive number.")

    def usage_percent(self):
        return round(self.used * 100 / self.TOTAL_MB)

    def status_lines(self):
        """Return the memory report as a list of text lines, with a usage bar."""
        bar_size = 30
        filled = round(bar_size * self.used / self.TOTAL_MB)
        bar = "#" * filled + "." * (bar_size - filled)
        return [
            f"Total Memory: {self.TOTAL_MB:>5} MB",
            f"Used Memory:  {self.used:>5} MB  (kernel {self.OS_RESERVED_MB} MB + you {self.allocated} MB)",
            f"Free Memory:  {self.free_mb:>5} MB",
            "",
            f"[{bar}] {self.usage_percent()}% used",
        ]
