from unittest import TestCase
from unittest.mock import patch
from project_0 import *
class TestStudent(TestCase):
     def setup(self):
       self.course = Course(1,'qa',1)
     def test_int_1(self):
       self.assertEqual(self.course.count_of_students)

     def test_add_student (self):
         student1=Student(123,'abc')
         student2=student(123,'abc')
         student3=Student(123,'abc')
         self.course.add_student(student1)
         self.course.add_student(student2)
         self.course.add_student(student3)
         self.assertEqual(self.course.students,student1)
         print(self.course)



