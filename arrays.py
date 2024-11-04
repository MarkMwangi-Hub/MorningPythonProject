#List has different datatypes while arrays are only of same datatypes

courses = ["MIT", "Cybersecurity", "Datascience"]
print(courses)

#Accessing an element in an array
print(courses[1])

#Looping through an array
for y in courses:
    print("Course is",y)

#Adding a new element to an array
courses.append("Android Development")
print(courses)

#Removing an element
courses.remove("MIT")
print(courses)
