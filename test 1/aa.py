from random import randint
num1=int(input(randint(1,50)))
num2=int(input("enter number 2: "))
num3: int=int(input("enter number 3: "))

if num1 > num2 and num1 > num3:
    print(num1)
if num2 > num3 and num2 > num1:
    print(num2)
if num3 > num2 and num3 > num1:
    print(num3)