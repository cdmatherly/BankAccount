class BankAccount:

    all_accounts = []

    def __init__(self, int_rate, balance):
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

Account_1 = BankAccount(0.035, 500)
Account_2 = BankAccount(0.045, 600)

Account_1.deposit(200).deposit(50).deposit(100).withdraw(500).yield_interest().display_account_info()
Account_2.deposit(300).deposit(100).withdraw(50).withdraw(75).withdraw(100).withdraw(10).display_account_info()

BankAccount.all_balances()