number = 25 #Int - This is an Integer used for numbers
second = 56.78 #float - This is a float used for decimal points
text = "Hello there" #String - This is a string used for characters
isPythonInteresting = True #This is a Boolean used for True or false values

#Data Structures - Multiple values stored in a single variable
cars = ["Toyota", "Nissan", "VW"] #This is a List. It uses [] - It is ordered and changeable
fruits = ("Banana", "Orange", "Apple") #This is a Tuple.It uses () - It is ordered but unchangeable
countries = {"Kenya","Tunisia","Algeria"} #This is a set. It uses {} - It is unordered and unchangeable
student = {
    #key : value
    "firstname" : "Mary",
    "age" : 34,
    "course" : "Web Development",
    "nationality" : "Kenyan"
} # This is a Dictionary. It uses {} with key and value pairs.

print(cars)
print(fruits)
print(countries)
print(student)
print(student["nationality"])

print(number)
print(second)
print(text)
print(isPythonInteresting)

#Determining a data type
print(type(countries))
print(type(student))
print(type(second))

# Typecasting - Process of converting from one datatype to another
print(float(number)) #prints integer "number" 25 as a float 25.0
print(int(second)) #prints float "second" 56.78 as an integer 56
