#Bài 1
chuoi = input("Chuỗi: ")
filename = input("Tên file: ")
f = open(filename, 'w')
f.write(chuoi)
f.close()

#Bài 2
filename = input("Tên file: ")
f = open(filename, 'r')
doc = f.read()
print(doc)
f.close()

#Bài 3
filename = input("Tên file: ")
chuoi = input("Chuỗi: ")
f = open(filename, 'a')
f.write(chuoi)
f.close()
#Bài 4
f = open(filename, 'r')
doc = f.read()
print(doc)
f.close()

#Bài 5
import random
list5 = []
check = 0
for i in range(1000):
    list5.append(random.randint(-1000, 1000))
filename = input("Tên file: ")
print(len(list5))
for i in list5:
    if check < 9:
        f = open(filename, 'a')
        f.write(str(i)+",")
        f.close()
        check +=1
    else:
        f = open(filename, 'a')
        f.write(str(i)+"\n")
        f.close()
        check = 0
f = open(filename, 'r')
a = f.readlines()
for i in a:
    print(i.replace(",", "    "))
f.close()