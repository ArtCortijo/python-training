# Lesson 20 - Bank Accounts
# custom error
class BalanceException(Exception):
    pass


class BankAccount():
    def __init__(self, initialBalance, accountName):
        self.balance = initialBalance
        self.accountName = accountName
        print(f"\nAccount {self.accountName} created. \nBalance = ${
              self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.accountName}' balance: ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"\nDeposit complete.")
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return True
        else:
            raise BalanceException(
                f"\nInsufficient funds. Account '{self.accountName}' balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print(f"\nWithdrawal complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdrawal failed: {error}")

    def transfer(self, amount, account):
        try:
            print(f"\n**********\n\nTransferring 💸")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print(f"\nTransfer complete! ✅\n\n**********")
        except BalanceException as error:
            print(f"\nTransfer failed 🙅‍♂️: {error}")


class InterestRewardsAccount(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print(f"\nDeposit complete. Interest added.")
        self.getBalance()


class SavingsAccount(InterestRewardsAccount):
    def __init__(self, initialBalance, accountName):
        super().__init__(initialBalance, accountName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("withdrawal complete")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdrawal failed: {error}")
