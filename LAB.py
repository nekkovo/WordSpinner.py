# Midterm 1 Lab Review
# How to make a bank account
class BankAccount:
    def __init__(self, name, starting_balance):
        full_name = name.split()  # split the full name
        # instance variables, always have the "self."
        self.first_name = full_name[0]  # first name
        self.last_name = full_name[1]  # last name
        self.balance = starting_balance
        self.history = []  # make a list to store our transactions

    # def makes different methods

    def acc_details(self):
        print(self.first_name + " " + self.last_name + " currently has: $" + str(self.balance), "in their account")

    def add_money(self, amount):
        self.balance += amount
        # self.balance = self.balance + amount
        self.history.append("+" + str(amount))
        print("$" + str(amount) + " has been inserted from your account")
        # using str() method to convert integer to a string

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            self.history.append("-" + str(amount))
            print("$" + str(amount) + " has been withdrawn from your account")

    def print_history(self):
        print(self.history)
def main():
    account1 = BankAccount("Lexie Dejilamu", 1000)
    account1.add_money(10000)
    account1.withdraw(12000)
    account1.acc_details()    # arguments
    # calling the method in the class


if __name__ == "__main__":
    main()
