## link: https://drive.google.com/file/d/1c0PK73q_xh0bby_GuqNtExFr33_qYLWL/view

from class_Student import *

"""
מאפייני המחלקה:
מספר קורס
שם קורס
רשימת נושאי לימוד ומרצים כשלכל נושא, יופיע שם המרצה שמלמד אותו
רשימת תלמידים
כמות תלמידים מקסימלית בקורס





שדרוג ל
add_student
לעשות בתוך המחלקה של קורס, פונקציה שמקבלת סטודנט ובודקת האם ניתן להכניס אותו לקורס,
כלומר,
אם הסטודנט לא קיים עדיין בקורס, ואם ברשימות הציונים שלו יש רק נושאים שקיימים בקורס.
מחזירה ערך בוליאני האם התלמיד יכול להיכנס לקורס או לא

לעדכן את הבדיקה ל- add_student


לעשות mock על הפונקציה למעלה
"""


class Course:
    def __init__(self, course_num, course_name, max_students):
        self.course_num = course_num
        self.course_name = course_name
        self.max_students = max_students
        self.lst_students = []
        self.subs_teachs = []

    def __str__(self):
        return f"{self.course_num}-{self.course_name} ->  \
                max students: {self.max_students}  \
                list of student({len(self.lst_students)}):  {self.lst_students}  \
                list of subjects and teachers({len(self.subs_teachs)}): {self.subs_teachs}"

    def __repr__(self):
        return f"{self.course_num}-{self.course_name} ->  \
                max students: {self.max_students}  \
                list of student({len(self.lst_students)}):  {self.lst_students}  \
                list of subjects and teachers({len(self.subs_teachs)}): {self.subs_teachs}"


    def is_student_suitable(self, student: Student):
        for subject in student.grades:
            for item in self.subs_teachs:
                if subject['subject'] == item['subject']:
                    break
                elif subject['subject'] != item['subject'] and self.subs_teachs.index(item) == len(self.subs_teachs)-1:
                    return False
        return True


    def add_student(self, student: Student):
        """
        :param student: a Student instance.
        :functionality: adds the student to a student list.
        :return: True or False, based on the max students for this course.
        """
        if len(self.lst_students) < self.max_students and self.is_student_suitable(student):
            self.lst_students.append(student)
            return True
        return False

    def add_factor(self, subject, fac_per):
        """
        :param subject: a subject name.
        :param fac_per: factor precentage.
        :functionality: changes all of this course's students' grades accordeing to the given factor.
                        max grade = 100
        :return: None
        """
        for student in self.lst_students:
            student.calc_factor(subject, fac_per)

    def del_student(self, id):
        """
        :param id: an existing student's id.
        :functionality: removes the student from the course.
        :return: None
        """
        for student in self.lst_students:
            if student.id == id:
                stud_index = self.lst_students.index(student)
                self.lst_students.pop(stud_index)
                break
        else:
            print(f"Trying to delete a student from the couse. Student's id: {id} not found")


if __name__ == '__main__':
    student1 = Student("Adam", 123)
    student1.grades = [
        {'subject': 'math', 'grade': 90},
        {'subject': 'SQL', 'grade': 75},
        {'subject': 'arts', 'grade': 80}
    ]
    course = Course(4, 'QA', 3)
    course.subs_teachs = [
        {'subject': 'math', 'teacher': 'Michal'},
        {'subject': 'Python', 'teacher': 'Orly'},
        {'subject': 'SQL', 'teacher': 'Yuval'}
    ]
    print(course.is_student_suitable(student1))
