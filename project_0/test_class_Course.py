from unittest import TestCase


class TestCourse(TestCase):
    def setup(self):
        self.course = Course(1, 'qa', 1)

    def test_int_1(self):
        self.assertEqual(self.course.count_of_student)
    def test_is_student_suitable(self):
        self.fail()




    def test_add_student(self):
        student1 = Student(123, 'abc')
        student2 = student(123, 'abc')
        student3 = Student(123, 'abc')
        self.course.add_student(student1)
        self.course.add_student(student2)
        self.course.add_student(student3)
        self.assertEqual(self.course.students.student1)



    def test_add_factor(self):
        self.fail()

    def test_del_student(self):
        self.fail()
