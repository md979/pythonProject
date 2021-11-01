def print_student(name,grade,*grades):
    if len(grades)==0:
        print(name,grade)
    else:
        print((grade+sum(grades))/(1+len(grades)))

print_student("Gal",75,88,99,100)
print_student("Gal",75)

def show_details(name,age,address='no address',*children,**additiona_details):
    print(name,age,address)
    print(children)
   # print(additiona_details)
    for i in additiona_details:
        print(additiona_details[i], end=' ')

show_details("dani",address="akjshdaksjdasd",age=30)
show_details("dani",25,"abcdefg",id=12345,phone="0541234567")
show_details("dani",25,"abcdefg",id=12345,phone="0541234567",profession='driver')
show_details("dani",25,"abcdefg","aaaa","bbbb","dddd",id=12345,phone="0541234567",profession='driver')

def f1(a,b=10,c=5,*args):
    print(a,b,c,args)
    return a+b+c

print(f1(10,11,7))
print(f1(10,11))
print(f1(10))
print(f1(10,c=12,b=11))
print(f1(10,11,12,1,2,3,4,5))