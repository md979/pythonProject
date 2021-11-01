class student:
    def __init__(self,id,name,grade):
        self.id=id
        self.name=name
        self.grade=grade
    def chek_pass(self):
        if self.grade>=70:
            return "true"
        else:
            return "false"

    def update_grade(self,factor):
        self.grade+=self.grade*factor/100
        if self.grade>100:
            self.grade=100
    def show(self):
        print(f'name:{self.name} id{self.id} {self.grade}')

student1=student(123,"abc",10)
student1.show()
if student1.chek_pass():
    print("studen pass")
else:
    print("student fail")






