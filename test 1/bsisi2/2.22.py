name=input("select name:")


words = name.split(' ')
character = ''
character2 = ''

xa=len(name)

for word in words:
   character += word[0]
   character2 += word[-1]

print((character+character2)*xa)



