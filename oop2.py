class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def movement(self):
        print("Person is walking")


a = Person("Joe",24,"Male")
print(a.name)
print(a.age)

b = Person("Mary",21,"Female")
print(b.name)
print(b.age)

c = Person("John",40,"Male")
print(c.name)
print(c.age)