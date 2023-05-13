name = input("Enter you name: ")

if len(name) < 3:
    print("Name must be atleast 3 charachters")
elif len(name) > 50:
    print("Name could not be greater than 50 characters")
else:
    print("Your name length is acceptable")

