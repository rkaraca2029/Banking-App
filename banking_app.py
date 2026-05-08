accounts = {
    "ACC001": {"name": "Alice Johnson", "balance": 1500.00, "pin": "1234"},
    "ACC002": {"name": "Bob Smith",     "balance": 850.50,  "pin": "5678"},
}


def get_account(account_id, pin):
    account = accounts.get(account_id)
    if not account:
        return None, "Account not found."
    if account["pin"] != pin:
        return None, "Incorrect PIN."
    return account, None


def deposit(account, amount):
    if amount <= 0:
        return False, "Deposit amount must be greater than zero."
    account["balance"] += amount
    return True, f"Deposited ${amount:.2f}. New balance: ${account['balance']:.2f}"


def withdraw(account, amount):
    if amount <= 0:
        return False, "Withdrawal amount must be greater than zero."
    if amount > account["balance"]:
        return False, f"Insufficient funds. Available balance: ${account['balance']:.2f}"
    account["balance"] -= amount
    return True, f"Withdrew ${amount:.2f}. New balance: ${account['balance']:.2f}"


def view_account(account):
    print(f"\n  Account Holder : {account['name']}")
    print(f"  Balance        : ${account['balance']:.2f}")


def main():
    print("=" * 40)
    print("        Welcome to PyBank")
    print("=" * 40)

    account_id = input("Enter account ID: ").strip()
    pin = input("Enter PIN: ").strip()

    account, error = get_account(account_id, pin)
    if error:
        print(f"\nError: {error}")
        return

    print(f"\nWelcome, {account['name']}!")

    while True:
        print("\n--- Menu ---")
        print("  1. View Account")
        print("  2. Deposit")
        print("  3. Withdraw")
        print("  4. Exit")

        choice = input("\nChoose an option (1-4): ").strip()

        if choice == "1":
            view_account(account)

        elif choice == "2":
            try:
                amount = float(input("Enter deposit amount: $"))
                success, message = deposit(account, amount)
                print(message)
            except ValueError:
                print("Invalid amount. Please enter a number.")

        elif choice == "3":
            try:
                amount = float(input("Enter withdrawal amount: $"))
                success, message = withdraw(account, amount)
                print(message)
            except ValueError:
                print("Invalid amount. Please enter a number.")

        elif choice == "4":
            print("\nThank you for banking with PyBank. Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1-4.")


if __name__ == "__main__":
    main()
