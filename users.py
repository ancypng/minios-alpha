"""Accounts and login for MiniOS Alpha.

This is a classroom demonstration only. Passwords are hashed, but the
accounts are hard-coded, so this is NOT real security.
"""
import getpass
import hashlib


def _hash(password):
    """Turn a password into a SHA-256 hash so it is not stored as plain text."""
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


class UserManager:
    MAX_ATTEMPTS = 3

    def __init__(self):
        self._accounts = {
            "admin": {"hash": _hash("admin123"), "role": "Administrator"},
            "student": {"hash": _hash("student123"), "role": "Standard User"},
        }
        self.current = None  # name of the logged-in user, or None

    def authenticate(self, username, password):
        """Return True (and log the user in) if the credentials are correct."""
        account = self._accounts.get(username)
        if account and account["hash"] == _hash(password):
            self.current = username
            return True
        return False

    def login_prompt(self):
        """Ask for credentials. Returns True on success, False after too many failures."""
        for attempt in range(1, self.MAX_ATTEMPTS + 1):
            username = input("Username: ").strip()
            password = self._ask_password()
            if self.authenticate(username, password):
                print(f"\n[OK] Login successful. Welcome, {username}!\n")
                return True
            attempts_left = self.MAX_ATTEMPTS - attempt
            print(f"\n[ERROR] Invalid username or password. ({attempts_left} attempt(s) left)\n")
        return False

    @staticmethod
    def _ask_password():
        """Read a password without showing it (falls back to plain input)."""
        try:
            return getpass.getpass("Password: ")
        except (EOFError, KeyboardInterrupt):
            raise  # let the shell handle Ctrl+C / Ctrl+Z
        except Exception:
            return input("Password: ")

    def logout(self):
        self.current = None

    def role(self):
        return self._accounts[self.current]["role"] if self.current else "None"

    def list_users(self):
        return [(name, account["role"]) for name, account in self._accounts.items()]
