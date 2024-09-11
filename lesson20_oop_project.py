from lesson20_bank_accounts import *

Art = BankAccount(100000, "Art")
Sara = BankAccount(50000, "Sara")

Art.getBalance()
Sara.getBalance()

Art.deposit(5000)
Sara.deposit(1000)

Art.withdraw(2000)

Art.transfer(5000, Sara)

Jim = InterestRewardsAccount(1000, "Jim")
Jim.getBalance()
Jim.deposit(500)
Jim.transfer(500, Sara)

Blaze = SavingsAccount(1000, "Blaze")
Blaze.getBalance()
Blaze.deposit(100)
Blaze.transfer(1000, Sara)
