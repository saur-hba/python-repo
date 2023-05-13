import os

filename = input("Enter filename: ")

if os.path.isfile(filename):
    if os.access(filename, os.W_OK):
        print("Enter text")
        with open(filename, "a") as f:
            f.write(input())
    else:
        print("No write permission")
else:
    print(f"{filename} does not exist")

