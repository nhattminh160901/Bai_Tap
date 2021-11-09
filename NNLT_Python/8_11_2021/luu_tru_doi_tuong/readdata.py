import pickle
f = open("Person", "rb")
print("Person\n", pickle.load(f))
f = open("Student", 'rb')
print("Student\n", pickle.load(f))
f = open("Professor", "rb")
print("Professor\n", pickle.load(f))