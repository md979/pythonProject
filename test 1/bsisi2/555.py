grd = int(input("Enter a grade: "))
sum, count = 0, 0
while 0 <= grd <= 100:
    if grd >= 60:
        count += 1
        sum += grd
    grd = int(input("enter a grade"))
print(f"the average of the passing tests is: {round(sum/count, 2)}")