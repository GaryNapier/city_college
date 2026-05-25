from transaction import Transaction


class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than 0.")
            return

        self.balance += amount

        transaction = Transaction("Deposit", amount, self.balance)
        self.transactions.append(transaction)

        print(f"£{amount:.2f} deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
            return

        if amount > self.balance:
            print("Insufficient funds.")
            return

        self.balance -= amount

        transaction = Transaction("Withdraw", amount, self.balance)
        self.transactions.append(transaction)

        print(f"£{amount:.2f} withdrawn successfully.")

    def show_balance(self):
        print(f"Current balance: £{self.balance:.2f}")

    def show_transactions(self):
        if not self.transactions:
            print("No transactions found.")
            return

        print("\nTransaction History:")
        for transaction in self.transactions:
            print(transaction)