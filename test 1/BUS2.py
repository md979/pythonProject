from bsisi2.bus3 import Person

class Bus_Persons:
    def __init__(self,num_of_seats):
        self.seats = [None for i in range(num_of_seats)]
        # self.seats=[]
        # for i in range(num_of_seats):
        #     self.seats.append("free")

        self.num_of_passengers=0

    def __str__(self):
        return f"{self.seats} number of passengers:{self.num_of_passengers}"

    def get_on(self,person:Person):
        if len(self.seats)>self.num_of_passengers:
            index_free=self.seats.index(None)
            self.seats[index_free]=person
            self.num_of_passengers+=1
        else:
            print(f"{person.name} can not get on the bus. It's full!!")

    def get_off(self,person:Person):
        if person in self.seats:
            index_person = self.seats.index(person)
            self.seats[index_person] = None
            self.num_of_passengers -= 1
        else:
            print(f"{person.name} is not on the bus!")

bus=Bus_Persons(10)
print(bus)

person1=Person(123,"Moshe",24)
bus.get_on(person1)
person2=Person(222,"Gili",30)
bus.get_on(person2)

print(bus)
person3=Person(222,"Gili",30)
bus.get_off(person3)
print(bus)