class Bus:
    def __init__(self,num_of_seats):
        self.seats = ["free" for i in range(num_of_seats)]
        # self.seats=[]
        # for i in range(num_of_seats):
        #     self.seats.append("free")

        self.num_of_passengers=0

    def __str__(self):
        return f"{self.seats} number of passengers:{self.num_of_passengers}"

    def get_on(self,name):
        if len(self.seats)>self.num_of_passengers:
            index_free=self.seats.index("free")
            self.seats[index_free]=name
            self.num_of_passengers+=1
        else:
            print(f"{name} can not get on the bus. It's full!!")

    def get_off(self,name):
        if name in self.seats:
            index_name = self.seats.index(name)
            self.seats[index_name]="free"
            self.num_of_passengers-=1
        else:
            print(f"{name} is not on the bus!")

bus=Bus(6)
print(bus)

bus.get_on("Dani")
print(bus)
bus.get_on("Shulamit")
print(bus)
bus.get_on("Gal")
print(bus)
bus.get_off("Shulamit")
print(bus)
bus.get_on("Beni")
print(bus)