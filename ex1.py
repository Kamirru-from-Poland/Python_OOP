class BankAccount:
    def __init__(self, account_name:str, account_number:int):
        self.account_name = account_name
        self.account_number = account_number
        self.balance = 0.0

    def display_balance(self):
        print(f"{self.account_number} {self.account_name}")
        print(f"current balance: {self.balance}")

# Lily Smith
account = BankAccount("LilySmith",9988887777)
account.display_balance()

