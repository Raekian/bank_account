class BankAccount:
    all_accounts = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    @classmethod
    def display_all(cls):
        for account in cls.all_accounts:
            print(account.int_rate, account.balance)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(self.int_rate, self.balance)
        return self

    def yield_interest(self):
        self.balance += (self.balance * self.int_rate)
        return self


steven = BankAccount(.02, 6000)
caleb = BankAccount(.04, 10000)

steven.deposit(1000).deposit(1000).deposit(1000).withdraw(3000).yield_interest().display_account_info()
caleb.deposit(1000).deposit(1000).withdraw(500).withdraw(500).withdraw(500).withdraw(500).yield_interest().display_account_info()
BankAccount.display_all()