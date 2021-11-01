first=input("eneter firs word:")
secon=input("eneter second word:")
if secon in first:
    for i in range(len(first)):
        if first[i]==secon:
            print(i)
            break


else:
    print(-1)





