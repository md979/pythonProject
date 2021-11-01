from random import  randint
list1=[randint(1,100) for i in range(10)]
print(list1)
t1=tuple(list1)
print(t1)
a=input('enter number;')
t1+=a,
print(t1)
t2=