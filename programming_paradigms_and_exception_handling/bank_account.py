class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = float(initial_balance)

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            # Formatting to .1f to match the [Expected] "67.0"
            print(f"Deposited: ${amount:.1f}")

    def withdraw(self, amount):
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            # Formatting to .1f to match the [Expected] "50.0"
            print(f"Withdrew: ${amount:.1f}")
            return True
        else:
            # Match the exact string "Insufficient funds."
            print("Insufficient funds.")
            return False

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.1f}")