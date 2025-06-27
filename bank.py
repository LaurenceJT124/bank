class BankAccount:

    title = "big_bank"

    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, interest_rate):

        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self.account_number = account_number
        self.routing_number = routing_number
        self.interest_rate = interest_rate

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
        print(f"Account Number: {self.account_number}")
        print(f"Routing Number: {self.routing_number}")
        print(f"Interest Rate: {self.interest_rate}")