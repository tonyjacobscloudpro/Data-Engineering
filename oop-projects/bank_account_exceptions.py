# bank_account_exceptions.py

# Features and Functionality:
# - Custom Exceptions:
#   Defines specific exceptions for invalid transactions such as insufficient funds and invalid amounts.
# - Error Handling:
#   Gracefully handles errors to provide meaningful messages to users.
# - Robust Transaction System:
#   Prevents invalid transactions like withdrawing more than the balance or depositing negative amounts.

# 1. Define Custom Exceptions
# - This section defines exceptions for invalid transactions.

print("1. Defining Custom Exceptions")

class InsufficientFundsError(Exception):
    """
    Raised when a withdrawal amount exceeds the available balance.
    """
    pass

class InvalidAmountError(Exception):
    """
    Raised when an invalid amount (negative or zero) is used in a transaction.
    """
    pass


# 2. Bank Account with Exception Handling
# - This section implements a BankAccount class that uses custom exceptions for error handling.

print("\n2. Implementing Bank Account with Exception Handling")

class BankAccount:
    """
    Represents a bank account with exception handling for invalid transactions.
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
            raise InvalidAmountError("Deposit amount must be greater than 0.")
        self.balance += amount
        self.transaction_history.append(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        print(f"Deposited ${amount:.2f}. Current balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        """
        Withdraws money from the account.
        :param amount: Amount to withdraw.
        """
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be greater than 0.")
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds for this withdrawal.")
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


# 3. Test the Bank Account with Exception Handling
# - This section demonstrates the functionality of the BankAccount class with invalid transactions.

print("\n3. Testing Bank Account with Exception Handling")

def test_bank_account_exceptions():
    # Create a new bank account
    account = BankAccount(account_holder="Alice Smith", initial_balance=100)

    try:
        # Perform valid transactions
        print("\nPerforming Valid Transactions:")
        account.deposit(50)          # Deposit $50
        account.withdraw(30)         # Withdraw $30

        # Perform invalid transactions
        print("\nAttempting Invalid Transactions:")
        account.withdraw(150)        # Withdraw more than balance
    except InsufficientFundsError as e:
        print(f"Error: {e}")

    try:
        account.deposit(-10)         # Deposit a negative amount
    except InvalidAmountError as e:
        print(f"Error: {e}")

    try:
        account.withdraw(0)          # Withdraw zero amount
    except InvalidAmountError as e:
        print(f"Error: {e}")

    # Display final balance and transaction history
    print(f"\nFinal Balance: ${account.get_balance():.2f}")
    account.print_transaction_history()


# Run the test
test_bank_account_exceptions()
