# bank_account.py

# Features and Functionality:
# - Object-Oriented Design:
#   Encapsulates the BankAccount functionality in a class.
# - Deposit and Withdrawal:
#   Allows depositing and withdrawing money with validation.
# - Transaction Summary:
#   Provides an account summary with balance and transaction history.

# 1. Bank Account Design
# - This section defines the core class for the Bank Account Manager.

print("1. Bank Account Manager Design")

class BankAccount:
    """
    Represents a bank account with basic deposit, withdrawal, and transaction history functionality.
    """
    def __init__(self, account_holder, initial_balance=0):
        """
        Initializes the bank account.
        :param account_holder: Name of the account holder.
        :param initial_balance: Initial balance for the account (default is 0).
        """
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transaction_history = []

        # Log the account creation
        self.transaction_history.append(f"Account created for {self.account_holder} with initial balance ${self.balance:.2f}")

    def deposit(self, amount):
        """
        Deposits money into the account.
        :param amount: Amount to deposit.
        """
        if amount <= 0:
            print("Deposit amount must be greater than 0.")
            return
        self.balance += amount
        self.transaction_history.append(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        print(f"Deposited ${amount:.2f}. Current balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        """
        Withdraws money from the account.
        :param amount: Amount to withdraw.
        """
        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
            return
        if amount > self.balance:
            print("Insufficient funds for this withdrawal.")
            return
        self.balance -= amount
        self.transaction_history.append(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        print(f"Withdrew ${amount:.2f}. Current balance: ${self.balance:.2f}")

    def get_balance(self):
        """
        Returns the current balance of the account.
        """
        return self.balance

    def print_transaction_history(self):
        """
        Prints the transaction history of the account.
        """
        print(f"\nTransaction History for {self.account_holder}:")
        for transaction in self.transaction_history:
            print(transaction)


# 2. Test the Bank Account Manager
# - This section demonstrates the functionality of the BankAccount class with test cases.

print("\n2. Testing the Bank Account Manager")

def test_bank_account():
    # Create a new bank account
    account = BankAccount(account_holder="John Doe", initial_balance=100)

    # Perform some transactions
    print("\nPerforming Transactions:")
    account.deposit(50)         # Deposit $50
    account.withdraw(30)        # Withdraw $30
    account.withdraw(150)       # Attempt to withdraw more than balance
    account.deposit(-10)        # Attempt to deposit a negative amount
    account.withdraw(20)        # Withdraw $20

    # Display current balance
    print(f"\nFinal Balance: ${account.get_balance():.2f}")

    # Display transaction history
    account.print_transaction_history()


# Run the test
test_bank_account()
