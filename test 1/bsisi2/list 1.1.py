from random import randint
list2= [randint(1,10) for i in range (10)]
print(list2)
print(list2[-3:])
print(list2[::-1])
for num in list2:

    if num % 2 == 0:
        print(num, end=" ")
 
list3= [1,5,8,9,85,5,88,5,9,23,65,12]
print(list3)