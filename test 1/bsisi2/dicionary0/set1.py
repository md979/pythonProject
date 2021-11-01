set1={10,20,30,40}
set2={5,20,35,40}
set3=set()
set3.update(set1)
set3.update(set2)
print(set3)
print(set3.pop())
print(max(set3),min(set3),len(set3))
set4=set()
set4.update(set3)
set4.update({82,45})
print(set4)

set1.clear()
set2.clear()
print(set1,set2)


