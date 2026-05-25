from account import Account


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        username = input("Enter username: ")

        if username in self.accounts:
            print("Username already exists.")
            return

        password = input("Enter password: ")

        account = Account(username, password)
        self.accounts[username] = account

        print("Account created successfully.")

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")

        account = self.accounts.get(username)

        if account and account.password == password:
            print(f"Welcome, {username}!")
            return account

        print("Invalid username or password.")
        return None