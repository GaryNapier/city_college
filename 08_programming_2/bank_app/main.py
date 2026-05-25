from bank import Bank


def logged_in_menu(account):
    while True:
        print("\n--- Account Menu ---")
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Check balance")
        print("4. Transaction history")
        print("5. Logout")

        choice = input("Choose an option: ")

        if choice == "1":
            try:
                amount = float(input("Enter withdrawal amount: £"))
                account.withdraw(amount)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "2":
            try:
                amount = float(input("Enter deposit amount: £"))
                account.deposit(amount)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "3":
            account.show_balance()

        elif choice == "4":
            account.show_transactions()

        elif choice == "5":
            print("Logging out...")
            break

        else:
            print("Invalid option.")


def main():
    bank = Bank()

    while True:
        print("\n=== Bank System ===")
        print("1. Create new account")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            bank.create_account()

        elif choice == "2":
            account = bank.login()

            if account:
                logged_in_menu(account)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()