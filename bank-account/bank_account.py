import threading


class BankAccount(object):
    def __init__(self):
        self.balance = None
        self.is_open = False
        self.lock = threading.Lock()

    def get_balance(self):
        with self.lock:
            if not self.is_open:
                raise ValueError('account not open')
            return self.balance

    def open(self):
        with self.lock:
            if self.is_open:
                raise ValueError('account already open')
            self.balance = 0
            self.is_open = True

    def deposit(self, amount):
        with self.lock:
            if not self.is_open:
                raise ValueError('account not open')
            if amount < 0:
                raise ValueError('amount must be positive')
            self.balance += amount

    def withdraw(self, amount):
        with self.lock:
            if not self.is_open:
                raise ValueError('account not open')
            if amount < 0:
                raise ValueError('amount must be positive')
            if amount > self.balance:
                raise ValueError('amount cannot be greater than balance')
            self.balance -= amount

    def close(self):
        with self.lock:
            if not self.is_open:
                raise ValueError('account not open')
            self.is_open = False
