from bank import BankAccount

class SavingsAccount(BankAccount):

    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, interest_rate ):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number, interest_rate)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.current_balance +=  self.interest_rate * self.interest_rate
