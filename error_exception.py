# age = int(input("Age is: "))
# print(age)

try:
    age = int(input("Age is: "))
    income = 20000
    risk = income/age
    print(age)
except ValueError:                                          #to prevent the crashing of code if the user enters age as some by mistake
    print("Invalid value")
except ZeroDivisionError:                                   #to prevent the crashing of code if the user enters age as 0 by mistake
    print("Age cant be zero")
