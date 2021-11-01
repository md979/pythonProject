list1=[]

for i in range(5):
    list1.append(int(input("enter number; ")))

    print (list1)

list2= [int(input("enter number; ")) for i in range (3)]
print(list2)
text= 'i love tlv'
list3=[i for i in text]



print(list3)