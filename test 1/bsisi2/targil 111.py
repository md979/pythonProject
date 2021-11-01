
def grades(name,grade,*optionalgrades):

    if len(optionalgrades)>0:
        return name,(sum(optionalgrades)+grade)/(len(optionalgrades)+1)
    return name,grade

print(grades("david",82))

def show_d(name,age,adress,*args,**mor_d):
    print(name,age,adress)
    print(args)
    print(mor_d)
    for i in mor_d:
        print(mor_d[i], end=' ')


show_d("miguel",24,"morad",id=33257,phone="05222")
show_d("miguel",24,"morad",id=33257,phone="05222",f_name="baba")


