"""Simulated memory management for MiniOS Alpha."""


class MemoryError_(Exception):
    pass


class MemoryManager:
    TOTAL_MB = 1024
    OS_RESERVED_MB = 256  # memory the "kernel" always uses

    def __init__(self):
        self.allocated = 0

    @property
    def used(self):
        return self.OS_RESERVED_MB + self.allocated

    @property
    def free_mb(self):
        return self.TOTAL_MB - self.used

    def allocate(self, mb):
        if mb <= 0:
            raise MemoryError_("Amount must be a positive number.")
        if mb > self.free_mb:
            raise MemoryError_(
                f"Not enough free memory. Only {self.free_mb} MB available."
            )
        self.allocated += mb

    def release(self, mb):
        if mb <= 0:
            raise MemoryError_("Amount must be a positive number.")
        if mb > self.allocated:
            raise MemoryError_(
                f"Cannot free {mb} MB. Only {self.allocated} MB is allocated by you."
            )
        self.allocated -= mb

    def status_lines(self):
        return [
            "Memory Status",
            "------------------------",
            f"Total Memory: {self.TOTAL_MB:>4} MB",
            f"Used Memory:  {self.used:>4} MB",
            f"Free Memory:  {self.free_mb:>4} MB",
        ]
