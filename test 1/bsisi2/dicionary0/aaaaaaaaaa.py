class Account:

    def __init__(self, name, number,overdraft_limit):
        self.name=name
        self.number=number
        self.balance=0
        self.overdraft_limit=overdraft_limit
        self.transactions=[]
        self.max_transactions=10

    def add_transaction(self,amount):
        # if len(self.transactions)<self.max_transactions:
        #     self.transactions.append(amount)
        # else:
        #     del self.transactions[0]
        #     self.transactions.append(amount)

        if len(self.transactions)>=self.max_transactions:
            #del self.transactions[0]
            self.transactions.pop(0)
        self.transactions.append(amount)

    def deposit(self, amount):
        if type(amount)!=int and type(amount)!=float:
            print("invalid type of amount")
            return
        if amount<0:
            print("invalid amount for deposit. must be positive")
            return

        self.balance+=amount
        self.add_transaction(amount)


    def withdraw(self, amount):
        if self.balance-amount<self.overdraft_limit:
            print("withdraw failed! Below the overdraft limit.")
        else:
            self.balance-=amount

        self.add_transaction(-amount)

    def __str__(self):
        return f"name: {self.name} account number:{self.number} balance: {self.balance} transactions:{self.transactions}"



# define an object called my_account of type Account


my_account=Account("orly",1234,-2000)
my_account.withdraw(1500)
# if my_account.balance<0:
#     print("balance is in overdraft")

print(my_account)

my_account.deposit(3000)
print(my_account)

my_account.withdraw(800)
print(my_account)
my_account.withdraw(10)
print(my_account)
my_account.withdraw(10)
print(my_account)
my_account.withdraw(10)
print(my_account)
my_account.withdraw(10)
print(my_account)
my_account.withdraw(10)
print(my_account)
my_account.withdraw(10)
print(my_account)
my_account.withdraw(10)
print(my_account)
my_account.withdraw(10)
print(my_account)
my_account.withdraw(10)
print(my_account)
my_account.withdraw(10)
print(my_account)


# your_account=Account("Anat",456,-500)
#
# your_account.balance=-900
#
# print(your_account)
#
# your_account.deposit(2000)
# print(your_account)
#
# your_account.withdraw(100)
# print(your_account)