try:
    print(number)
except:
    print("An Error has occurred")



try:
    num1 = 39
    num2 = 3
    print(num1/num2)
except:
    print("Zero Division Error has occured")
finally:
    print("Success")