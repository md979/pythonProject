## link: https://drive.google.com/file/d/1c0PK73q_xh0bby_GuqNtExFr33_qYLWL/view

from class_Student import *
from class_Course import *
"""
יש לכתוב תכנית ראשית שתבצע את הפעולות הבאות:
 - תיצור אובייקט קורס עם הנתונים: מס',שם קורס ומס' תלמידים  מקסמילי (יתקבלו כקלט מהמשתמש)

- תקלוט נושאים ולכל נושא – שם מרצה. הנתונים ייכנסו למילון  באובייקט הקורס.

- תקלוט מספרי ת.ז. של סטודנטים בלולאה כל עוד נקלט מס' השונה מ- 0 וכל עוד יש מקום בקורס.
 עבור כל ת.ז. , יש לקלוט שם ולאחר מכן  לקלוט ציונים של הסטודנט עבור כל נושא בקורס ולהכניס אותו לרשימת  הציונים של הסטודנט.
  כשסיימנו לקלוט ציונים , נכניס את הסטודנט לקורס.
   אם הכנסת הסטודנט לקורס נכשלה (התקבל False), יש לסיים  את קליטת הסטודנטים.

- כעת התכנית תקלוט נושא שעליו יחושב פקטור ואחוז פקטור.
 התכנית  תעבור על כל התלמידים ותחשב ציון חדש לנושא הרלוונטי בהתאם  לפקטור.

- בשלב הבא, התכנית תמצא מיהו הסטודנט עם הממוצע הנמוך ביותר  ותמחק אותו מהקורס.
 אם נמצאו מס' סטודנטים עם ממוצע נמוך זהה,  יימחקו כולם.

- לסיום, התכנית תדפיס את כל הקורס, כולל המרצים, התלמידים  והציונים שלהם.

"""


def enter_subjects(course: Course):
    print(f"Entering a new subject to the course '{course.course_name}'.")
    entering_subjects = True
    while entering_subjects:
        subject_name = input("Enter the subject's name: ")
        teacher_name = input(f"Enter the subject {subject_name}'s teacher's name: ")
        course.subs_teachs.append(
            {
                'subject': subject_name,
                'teacher': teacher_name
            }
        )
        print(f"--The subject {subject_name}, learned by {teacher_name} entered to the course {course.course_name}.--")
        entering_subjects = int(input(
                    f"Would you like to enter another subject to the course '{course.course_name}'?\n \
                    Yes- 1 \n \
                    No- 0 \n \
                    Your Choice: " or 1
                ))


def add_students(course: Course):
    room_counter = course.max_students
    print(f"Entering a new student to the course {course.course_name}.")
    new_id = int(input("Enter the student's id: ")) or 0  # entering 0 will exit the loop
    while new_id and room_counter > 0:
        stud_name = input(f"Enter a name to the student with id: {new_id}:  ") or "no_name"
        new_student = Student(stud_name,new_id)
        for subject in course.subs_teachs:
            grade = int(input(f"Enter a grade for the student '{stud_name}' in the subject '{subject['subject']}':  ")) or 0
            new_student.add_grade(subject['subject'],grade)
        if not course.add_student(new_student):
            print(f"Line 76: Did not enter {new_student.name} to the course. ")
            break;
        print(f"Entering a new student to the course {course.course_name}.")
        new_id = int(input("Enter the student's id: ")) or 0  ## entering 0 will exit the loop
    print(f"All done. the scourse's students list so far: ", course_01.lst_students)


def calc_factor(course: Course):
    print(f"Entering a factor to the course {course.course_name}'s students.")
    fac_sub = input("Enter a subject: ")
    fac_per = int(input("Enter the factor precentage: "))
    course.add_factor(fac_sub, fac_per)


def dismiss_student(course: Course):
    lowest_avg = 100
    for student in course.lst_students:
        student_ave = student.average()
        if student_ave < lowest_avg:
            lowest_avg = student_ave
    for student in course.lst_students:
        if student.average() == lowest_avg:
            stud_index = course.lst_students.index(student)
            course.lst_students.pop(stud_index)


def get_course(course:Course):
    print(course)


## ________________________________________________________________________________________________________________________


# course_num = int(input("Enter the course's number: "))
# course_name = input("Enter the course's name: ")
# max_students = int(input("Enter the course's maximum students capacity: "))
#
# course_01 = Course(course_num,course_name,max_students)

course_01= Course(4,'QA automation',2)

enter_subjects(course_01)
print(course_01.subs_teachs)
add_students(course_01)
calc_factor(course_01)
dismiss_student(course_01)
get_course(course_01)
