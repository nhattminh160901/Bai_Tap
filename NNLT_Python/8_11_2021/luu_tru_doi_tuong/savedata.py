import pickle
import random

class Person:
  def __init__(self, name, phoneNumber, email):
    self.name = name
    self.phoneNumber = phoneNumber
    self.email = email

class Student(Person):
  def nhapDuLieu(self, stuNumber, aveMark):
    self.stuNumber = stuNumber
    self.aveMark = aveMark

class Professor(Person):
  def nhapDuLieu(self, salary):
    self.salary = salary


#Lưu danh sách Person
per = []
for i in range(10):
  name = input("Nhập tên: ")
  phone = random.randint(10000000, 15000000)
  email = name+"@gmail.com"
  per.append(Person(name, phone, email).__dict__)
print("Person:\n", per)
newper = sorted(per, key=lambda k:k['name'], reverse=True)
f = open('Person', 'wb') 
pickle.dump(newper, f)

#Lưu danh sách Student
list_first_name = ["Tri","Minh","Huy","Pro","Hi","Hayate", "Max", "Gwen"]
list_Last_name = ["Nguyen", "Ho", "Tran", "Ly", "Le", "Stacy"]
stu = []
for i in range(10):
  name = random.choice(list_first_name)+" "+random.choice(list_Last_name)
  phone = random.randint(10000000,15000000)
  email = f'{name}@gmail.com'.replace(" ","")
  stuNumber = random.randint(20000000,30000000)
  aveMark = random.randint(0, 10)
  student_sample = Student(name, phone, email)
  student_sample.nhapDuLieu(stuNumber, aveMark)
  stu.append(vars(student_sample))
print("Student:\n", stu)
newstu = sorted(stu, key=lambda k:k['aveMark'], reverse=True)
f = open('Student', 'wb') 
pickle.dump(newstu, f)

#Lưu danh sách Professor
pro = []
for i in range(10):
  name = random.choice(list_first_name)+" "+random.choice(list_Last_name)
  phone = random.randint(10000000,15000000)
  email = f'{name}@gmail.com'.replace(" ","")
  salary = random.randint(6000000, 30000000)
  professor_sample = Professor(name, phone, email)
  professor_sample.nhapDuLieu(salary)
  pro.append(vars(professor_sample))
print("Professor:\n", pro)
newpro = sorted(pro, key=lambda k:k['salary'], reverse=False)
f = open('Professor', 'wb') 
pickle.dump(newpro, f)
