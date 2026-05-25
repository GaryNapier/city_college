from datetime import datetime


class Transaction:
    def __init__(self, transaction_type, amount, balance):
        self.transaction_type = transaction_type
        self.amount = amount
        self.balance = balance
        self.timestamp = datetime.now()

    def __str__(self):
        return (
            f"[{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}] "
            f"{self.transaction_type}: £{self.amount:.2f} | "
            f"Balance: £{self.balance:.2f}"
        )