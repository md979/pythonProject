word = input("enter word:")

characters = "A a"

word = ''.join(I for I in word if I not in characters)
print(word)