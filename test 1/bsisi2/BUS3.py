class Person:
    # Constrcutor
    def __init__(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age

    def __str__(self):
        return f"{self.name} id:{self.id} age:{self.age}"

    def __repr__(self):
        return f"{self.name} id:{self.id} age:{self.age}"

    def __eq__(self, other):
        if type(other) != Person :
            return False

        if self.id==other.id and self.name==other.name:
            return True
        else:
            return False


# a=5
#
#
# person1=Person(123,"Moshe",24)
# person2=Person(222,"Gili",30)
# person3=Person(333,"Yigal",49)
# person4=Person(222,"Gili",30)
#
# persons = [person1,None,person2,person3,None]
# print(persons)
#
# print(person4 in persons)
# #print(person1==person2)
# #print(person1==person4)
