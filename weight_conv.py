weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print(f"Your weight is: {converted} pounds")
else:
    converted = weight * 0.45
    print(f"Your weight is {converted} kilograms")


# weight_lbs = input("What is your weight in lbs? ")
# weight_kgs = float(weight_lbs) * 0.45
# print(weight_kgs)