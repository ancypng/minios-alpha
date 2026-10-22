# logins
import getpass
import hashlib


def _hash(password):
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


class UserManager:
    MAX_ATTEMPTS = 3

    def __init__(self):
        # Password
        self._accounts = {
            "admin": {"hash": _hash("admin123"), "role": "Administrator"},
            "student": {"hash": _hash("student123"), "role": "Standard User"},
        }
        self.current = None

    def authenticate(self, username, password):
        account = self._accounts.get(username)
        if account and account["hash"] == _hash(password):
            self.current = username
            return True
        return False

    def login_prompt(self):
        """Ask for credentials. Returns True on success, False after too many failures."""
        for attempt in range(1, self.MAX_ATTEMPTS + 1):
            username = input("Username: ").strip()
            try:
                password = getpass.getpass("Password: ")
            except (EOFError, KeyboardInterrupt):
                raise
            except Exception:
                password = input("Password: ")
            if self.authenticate(username, password):
                print("\nLogin successful.\n")
                print(f"Welcome, {username}!")
                return True
            left = self.MAX_ATTEMPTS - attempt
            print(f"\nError: Invalid username or password. ({left} attempt(s) left)\n")
        return False

    def logout(self):
        self.current = None

    def role(self):
        return self._accounts[self.current]["role"] if self.current else "None"

    def list_users(self):
        return [(name, acc["role"]) for name, acc in self._accounts.items()]
