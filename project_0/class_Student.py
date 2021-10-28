
## link: https://drive.google.com/file/d/1c0PK73q_xh0bby_GuqNtExFr33_qYLWL/view
"""
מאפייני המחלקה:
תעודת זהות
שם
רשימה של נושאי לימוד וציונים(תכיל מילון)


"""
class Student:
    def __init__(self,name,id):
        self.name = name
        self.id = id
        self.grades = []

    def __str__(self):
        return f"{self.name} ->  id: {self.id}\
                grades({len(self.grades)}): {self.grades} "

    def __repr__(self):
        return f"{self.name} ->  id: {self.id}\
                grades({len(self.grades)}): {self.grades} "


    def add_grade(self,subject,grade):
        """
        :param subject: study subject
        :param grade: the subject's grade
        :functionality: adds the subject and the grade to the stodent's grades list
        :return: None
        """
        self.grades.append(
            {
            "subject": subject,
            "grade": grade
            }
        )

    """
    !!! מה אם הציון לא קיים עדיין ברשימת הציונים של התלמיד? !!!
    """
    def calc_factor(self,subject,fac_per):
        """
        :param subject: study subject
        :param fac_per: factor precentage
        :fucntionality: adds the factor to the subject's grade. max grade = 100.
        :return: None
        """
        for item in self.grades:
            if item['subject'] == subject:
                new_grade = item['grade'] + (item['grade'] * fac_per) / 100
                if new_grade >= 100:
                    item['grade'] = 100
                else:
                    item['grade'] = new_grade
                break
        else:
            return f"the subject '{subject}' was not found in {self.name}'s grades list."


    def average(self):
        """
        :return: average of the student's grades.
                 returns 0 if none were entered.
        """
        if len(self.grades) == 0:
            print(f"Trying to calculate average of {self.name}'s grades. No grades were entered yet.")
            return 0

        sum = 0
        for item in self.grades:
            sum += item['grade']

        return sum / len(self.grades)


if __name__== '__main__':
    ## will only run if this file was ran directly, and not from an import.
    ## this file's __name__ in case it was imported: 'class_Student'
    new_stud = Student("Adam",123)
    new_stud.add_grade('math',99)
    print(new_stud.grades)
    new_stud.calc_factor('arts',10)
    print(new_stud.grades)
    new_stud1 = Student("Eve",124)
    help(new_stud1.calc_factor)
    print([new_stud1,new_stud])