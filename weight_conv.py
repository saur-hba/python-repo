weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in pounds is: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in kgs is: " + str(converted))


# weight_lbs = input("What is your weight in lbs? ")
# weight_kgs = float(weight_lbs) * 0.45
# print(weight_kgs)