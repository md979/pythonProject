def between( x, y, z):
   if x > y:
       return x
   return "false"

def between(x, y, z):

   if x < z:
       return x
   return "false"


x = int(float(input("choise number")))
y = int(float(input("litlle number")))
z = int(float(input('big number')))
print(between(x,y,z))
