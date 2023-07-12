class Account:
    name = "John"
    account_number = 27767289183766
    account_balance = 1000000

    def __init__(self):
        self.name = Account.name
        self.account_number = Account.account_number
        self.account_balance = Account.account_balance

    def deposit(self, amount):
        self.account_balance += amount
        print(f'Deposited {amount} dollars. New balance is {self.account_balance} dollars.')

class SavingsAccount(Account):
    interest_rate = 0.05
    min_balance = 1000

    def __init__(self):
        super().__init__()
        self.withdraw_count = 0

    def withdraw(self, amount):
        if amount > self.account_balance - SavingsAccount.min_balance:
            print("Withdrawal amount exceeds available balance or minimum balance required.")
            return
        if self.withdraw_count >= 3:
            print("Withdrawal limit reached for this month.")
            return
        self.account_balance -= amount
        self.withdraw_count += 1
        print(f'Withdrew {amount} dollars. New balance is {self.account_balance} dollars.')

    def calculate_interest(self):
        interest = self.account_balance * SavingsAccount.interest_rate
        self.account_balance += interest
        print(f'Interest earned: {interest:.2f} dollars. New balance is {self.account_balance} dollars.')

    def reset_withdraw_count(self):
        self.withdraw_count = 0
        print("Withdrawal count reset for this month.")

class BankAccount:
    def __init__(self, account_number, account_balance=0):
        self.account_number = account_number
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount
        return f"${amount} deposited successfully!"

    def withdraw(self, amount):
        if self.account_balance < amount:
            return "Insufficient funds!"
        else:
            self.account_balance -= amount
            return f"${amount} withdrawn successfully!"

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_balance=0, interest_rate=0.01):
        super().__init__(account_number, account_balance)
        self.interest_rate = interest_rate
        
    def add_interest(self):
        interest = self.account_balance * self.interest_rate
        self.account_balance += interest
        return f"${interest:.2f} interest added successfully!"
