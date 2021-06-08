class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def user_deposit(self, x):
        self.account.deposit(x)
        print("account balance is", self.account.balance)

    def user_withdraw(self, x):
        self.account.withdraw(x)
        print("account balance is", self.account.balance)

    def user_display(self):
        self.account.display_balance()

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

    def display_balance(self):
        print(self.balance)

    def display_account_info(self):
        print(self.int_rate, self.balance)
        return self

    def yield_interest(self):
        self.balance += (self.balance * self.int_rate)
        return self


steven = User("steven", "Steven@gmail.com")
caleb = User("caleb", "caleb@gmail.com")

steven.user_deposit(1000)
steven.user_withdraw(500)
steven.user_display()

# steven.deposit(1000).deposit(1000).deposit(1000).withdraw(3000).yield_interest().display_account_info()
# caleb.deposit(1000).deposit(1000).withdraw(500).withdraw(500).withdraw(500).withdraw(500).yield_interest().display_account_info()
# BankAccount.display_all()