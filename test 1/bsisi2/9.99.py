
word1 = input("enter word")
word2 = input("enter word")
word = word1+word2
prev = word[0]
sum = 1
for i in word[1::1]:
    if i == word:
        sum += 1
    else:
        print(prev, sum)
        sum = 1
    prev = i






