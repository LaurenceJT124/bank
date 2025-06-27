from CheckingAccount import CheckingAccount
from SavingsAccount import SavingsAccount

save_one = SavingsAccount("person_one",500,100,"123","321",0.01)
save_two = SavingsAccount("person_two",600,200,"456","654",0.02)
check_one = CheckingAccount("person_one_check", 100, 100, "678", "876", 200)
check_two = CheckingAccount("person_two_check", 1200, 200, "890", "098", 300)



#user puts money in saving and then interest applies
save_one.info()
save_one.deposit(300)
save_one.apply_interest()
save_two.info()
