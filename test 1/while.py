grade= int(input("enter grade: "))

while grade<0 or grade>100:
    print("invalid")
    grade = int(input('enter grade: '))

print("valid grade")