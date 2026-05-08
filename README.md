# PyBank - Banking App

A simple command-line banking application built in Python.

## Features

- **Account Access** — Log in securely with your account ID and PIN
- **View Account** — Check your account holder name and current balance
- **Deposit** — Add funds to your account
- **Withdraw** — Remove funds with automatic balance validation

## Demo Accounts

| Account ID | PIN  | Starting Balance |
|------------|------|-----------------|
| ACC001     | 1234 | $1,500.00       |
| ACC002     | 5678 | $850.50         |

## How to Run

Make sure you have Python 3 installed, then run:

```bash
python3 banking_app.py
```

## Usage

1. Enter your **Account ID** and **PIN** to log in
2. Choose from the menu:
   - `1` — View account details and balance
   - `2` — Make a deposit
   - `3` — Make a withdrawal
   - `4` — Exit

## Example

```
========================================
        Welcome to PyBank
========================================
Enter account ID: ACC001
Enter PIN: 1234

Welcome, Alice Johnson!

--- Menu ---
  1. View Account
  2. Deposit
  3. Withdraw
  4. Exit
```

## Built With

- Python 3
