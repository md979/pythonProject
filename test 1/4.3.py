from random import randint
num = randint(1.9)
guess= int(input("enter number betwen 1,9:"))

 while guess!=num:
     if guess<num:
        print("small")
     else:
         print('big')
         guss=int(input("enter your guss: "))
 print(correct)

