num=int(input("new number: "))

while num<100 or num>1000:
    print("invalid")
    num=(input("new number: "))

print(num)