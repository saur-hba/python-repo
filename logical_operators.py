# price = 5
# print(price > 10 and price < 30)
# print(price > 10 or price < 30)
# print(not price > 10)

# and (both operations true)
# or (atleast one true)
# not (reverses the output)


high_income = True
good_credit = True

if high_income and good_credit:
    print("You are eligible for the loan")

else:
    print("Sorry try again after 90 days")

high_income = True
good_credit = False

if high_income and good_credit:
    print("You are eligible for the loan")

else:
    print("Sorry try again after 90 days")

high_income = True
good_credit = False

if high_income or good_credit:
    print("You are eligible for the loan")

else:
    print("Sorry try again after 90 days")

high_income = False
good_credit = False

if high_income or good_credit:
    print("You are eligible for the loan")

else:
    print("Sorry try again after 90 days")