class Student:

    def __init__(self, name, id, scores=None):
        self.name = name
        self.id = id
        if scores:
            self.scores = scores
        else:
            self.scores = []


    def average(self):
        return sum(self.scores) / len(self.scores)


class Classroom:

    def __init__(self, name, students=None):
        self.name = name
        self.students = students if students else []

    def average(self):
        scores = []
        for student in self.students:
            scores += student.scores
        return sum(scores) / len(scores)


if __name__ == '__main__':
    john = Student("John smith", "0102030405", scores=[12, 13])
    jim = Student("Jim Morison", "0506070809", scores=[13, 15, 18])
    math = Classroom("math", students=[john, jim])

    print(john.name + " average is " + str(john.average()))
    print("{} average is {:2.2f}.".format(jim.name, jim.average()))
    print(f"The average of '{math.name}' class is {math.average}.")

    print(john.id)
    john.id = "0101010101"
    print(john.id)

    print(type(john), type(math))





