class Account:

    def __init__(self, name, number):
        self.name=name
        self.number=number
        self.balance=0
        self.overdraft_limit=-1000

    def deposit(self, amount):
        self.balance+=amount

    def withdraw(self, amount):
        if self.balance-amount<self.overdraft_limit:
            print("withdraw failed! Below the overdraft limit.")
        else:
            self.balance-=amount

    def show(self):
        print(f"name: {self.name} account number:{self.number} balance: {self.balance}")


# define an object called my_account of type Account
my_account=Account("orly",1234)

my_account.balance=1000

my_account.show()

my_account.deposit(200)
my_account.show()

my_account.withdraw(800)
my_account.show()

your_account=Account("Anat",456)

your_account.balance=-900

your_account.show()

# your_account.deposit(2000)
# your_account.show()

your_account.withdraw(100)
your_account.show()




