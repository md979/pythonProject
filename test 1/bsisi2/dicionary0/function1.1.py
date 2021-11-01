

def like_len(list):
    count = 0
    for i in list:
        count += 1
    return count

list3=[20,30,40,50]

print("The total number of elements in the list: ", like_len(list3))


def count_substring(list):

    a=0
    for i in range(like_len(list)):
        if(i== i):
            a += 1
    return a
lista=[20,40,50,20,50]

print(count_substring(lista))

def max_sub(num1, num2):


        if (num1<num2):
            return num1
        else:return num2


num1=25
num=30
print(max_sub(num,num1))

def grades(name,grade,*optionalgrades):

    if len(optionalgrades)>0:
        return name,sum(grade)/len(optionalgrades)
        return name,grades

    print(grades("miguel",100,88,90))











