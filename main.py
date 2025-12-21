class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance

if __name__ == "__main__":
    # Simple manual test
    account = BankAccount(100)
    account.deposit(50)
    print(f"Current Balance: {account.get_balance()}")