# Get 5 prices from the user, calculate sum and average of the products
# If the sum becomes higher than 200, we stop the loop

sum=0
count=0

for i in range(5):
    price = int(input("enter price: "))
    sum+=price
    count+=1
    print("sum:",sum,"count:",count)
    if sum>200:
        print("We reached sum: over 200!!!! We stop the shopping.")
        break

print("sum:",sum, "average:",sum/count)