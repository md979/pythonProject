


class person:


    def __init__(self, name, number):
        self.name = name
        self.num = number
        self.numberchildren = 0


    def show(self):
        print(f"name: {self.name} age:{self.num} number of children: {self.numberchildren}")


my_person = person("miguel", 24)
my_person.numberchildren = 2


my_person.show()



