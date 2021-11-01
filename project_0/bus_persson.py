from project_0.person import Person

class Bus_Persons:
    def __init__(self,num_of_seats):
        if type(num_of_seats)!=int:
            raise TypeError("Argument num of seats must be int.")

        if num_of_seats<=0:
            raise ValueError("Argument num of seats must be positive.")

        self.seats = [None for i in range(num_of_seats)]
        # self.seats=[]
        # for i in range(num_of_seats):
        #     self.seats.append("free")

        self.num_of_passengers=0

    def __str__(self):
        return f"{self.seats} number of passengers:{self.num_of_passengers}"

    #  method that gets a person on the bus
    def get_on(self,person:Person):
        'A person Gets on the bus'
        if type(person)!=Person:
            raise TypeError("Argument to get_on must be of type Person.")

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

if __name__=="__main__":
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