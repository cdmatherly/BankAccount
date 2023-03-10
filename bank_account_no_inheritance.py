#Create Bank Account class
class BankAccount:

    all_accounts = []

    def __init__(self, type, int_rate, balance):
        self.type = type
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance - amount > 0:
            self.balance -= amount
            return self
        print("Insufficient funds: Charging a $5 fee")
        self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance*self.int_rate
            return self
        return self

    @classmethod
    def all_balances(cls):
        for account in cls.all_accounts:
            account.display_account_info()

#Create User class that creates a bank account 
class User:
    def __init__(self, name, email, type):
        self.name = name
        self.email = email
        if type == 'checking':
            int_rate = 0.02
        elif type == 'savings':
            int_rate = 0.04
        else:
            int_rate = 0.00
        self.account = BankAccount(type, int_rate, balance=0)

    # def open_account(self, type, int_rate, balance):
    #     super().__init__(type, int_rate, balance)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        if self.account.balance > amount:
            self.account.balance -= amount
            return self

    def display_user_balance(self):
        print(self.account.balance)
        return self

    # ? How to specify which account is being withdrawn from?
    # def create_account(self, account_name, int_rate, balance):
    #     self.account = account_name
    #     account_name = BankAccount(int_rate, balance)
    #     return self


Account_1 = BankAccount("checking", 0.035, 500)
Account_2 = BankAccount("savings", 0.045, 600)

Account_1.deposit(200).deposit(50).deposit(100).withdraw(500).yield_interest().display_account_info()
Account_2.deposit(300).deposit(100).withdraw(50).withdraw(75).withdraw(100).withdraw(10).display_account_info()

# Grab all accounts and run display info
BankAccount.all_balances()

User_1 = User("Chase", "email@gmail.com", 'savings')
# User_1.open_account("checking", 0.01, 0)
# User_1.make_deposit(100)
User_1.display_user_balance()

print(User_1.account.int_rate)