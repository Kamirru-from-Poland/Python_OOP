class BankAccount:
    def __init__(self, account_name:str, account_number:int):
        self.account_name = account_name
        self.account_number = account_number
        self._balance = 0.0

    def display_balance(self):
        print(f"{self.account_number} {self.account_name}")
        print(f"current balance: {self._balance}")

    def deposit(self, amount):
        self._balance += amount
        print(f"You have deposited {amount}")

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            print(f"You have withdrawn {amount}")
        else:
            print("withdraw over balance is forbidden")

    def fee(self):
        pass

# Lily Smith
account = BankAccount("LilySmith",9988887777)
account.display_balance()
account.deposit(200)
account.deposit(50)
account.display_balance()
account.withdraw(75)
account.display_balance()
account.withdraw(500)