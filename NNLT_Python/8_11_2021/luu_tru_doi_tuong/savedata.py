import pickle
import random

class Person:
  def __init__(self, name, phoneNumber, email):
    self.name = name
    self.phoneNumber = phoneNumber
    self.email = email

class Student(Person):
  def __init__(self, name, phoneNumber, email, stuNumber, aveMark):
    super().__init__(name, phoneNumber, email)
    self.stuNumber = stuNumber
    self.aveMark = aveMark

class Professor(Person):
  def __init__(self, name, phoneNumber, email, salary):
    super().__init__(name, phoneNumber, email)
    self.salary = salary


#Lưu danh sách Person
per = []
for i in range(10):
  name = input("Nhập tên: ")
  phone = random.randint(10000000, 15000000)
  email = name+"@gmail.com"
  per.append(Person(name, phone, email).__dict__)
print("Person:\n", per)
newper = sorted(per, key=lambda k:k["name"], reverse=True)
f = open("Person", "wb") 
pickle.dump(newper, f)
f.close()

#Lưu danh sách Student
list_first_name = ["Tri","Minh","Huy","Pro","Hi","Hayate", "Max", "Gwen"]
list_Last_name = ["Nguyen", "Ho", "Tran", "Ly", "Le", "Stacy"]
stu = []
for i in range(10):
  name = random.choice(list_first_name)+" "+random.choice(list_Last_name)
  phone = random.randint(10000000,15000000)
  email = f"{name}@gmail.com".replace(" ","")
  stuNumber = random.randint(20000000,30000000)
  aveMark = random.randint(0, 10)
  student_sample = Student(name, phone, email, stuNumber, aveMark)
  stu.append(vars(student_sample))
print("Student:\n", stu)
newstu = sorted(stu, key=lambda k:k["aveMark"], reverse=True)
f = open("Student", "wb") 
pickle.dump(newstu, f)
f.close()

#Lưu danh sách Professor
pro = []
for i in range(10):
  name = random.choice(list_first_name)+" "+random.choice(list_Last_name)
  phone = random.randint(10000000,15000000)
  email = f"{name}@gmail.com".replace(" ","")
  salary = random.randint(6000000, 30000000)
  professor_sample = Professor(name, phone, email, salary)
  pro.append(vars(professor_sample))
print("Professor:\n", pro)
newpro = sorted(pro, key=lambda k:k["salary"], reverse=False)
f = open("Professor", "wb") 
pickle.dump(newpro, f)
f.close()