class Student:
    #Properties/Variables/Characteristics/Attributes
    name = "Mark"
    age = 21

    #Behaviours/Methods/Functions
    def study(self):
        print("Student is studying")

student1 = Student() #creating an object
student1.study()

print(student1.name)