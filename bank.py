class BankAccount:

    title = "BigBank"

    def __init__(self, customer_name, current_balance, minimum_balance):
        # Instance attributes
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

    def deposit(self, amount):
        self.current_balance += amount

    def withdraw(self, amount):
        if self.current_balance - amount < self.minimum_balance:
            print("Not enough funds")
        else:
            self.current_balance -= amount

    def info(self):
        print(f"Bank: {self.title}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Current Balance: {self.current_balance}")
        print(f"Minimum Balance: {self.minimum_balance}")