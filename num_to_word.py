phone = input("Enter your phone number: ")
digits_mapping = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
}
output = ""
for number in phone:
    output = output+digits_mapping.get(number, "!") + " "
    # output += digits_mapping.get(number, "!") + " "
print(output)