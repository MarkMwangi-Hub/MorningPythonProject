#Built-in Library Functions
y = max (67,77,89,66,54)
print(y)

x = min(77,55,24,5,88)
print(x)

z = pow(2,3)
print(z)

#User-defined Functions
def greeting ():
    print("Hello there!")

greeting()#calling a function.

def multiply():
    num1 = 23
    num2 = 10
    print(num1*num2)

multiply()

#Parameters/variable and Arguments/values assigned
def add( a, b):
    print (a+b)

add(3,4)
add(60,20)
add(150,50)

def employee (fullname,age,position,status):
     print(fullname,age,position,status)

employee("Mark Joe",27, "CEO","Married")
employee("Mary Jane",35, "HR","Single")
employee("Job Harry",60, "Clerk","Married")
