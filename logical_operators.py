# price = 5
# print(price > 10 and price < 30)
# print(price > 10 or price < 30)
# print(not price > 10)

# and (both operations true)
# or (atleast one true)
# not (reverses the output)


# high_income = True
# good_credit = True

# if high_income and good_credit:
#     print("You are eligible for the loan")

# else:
#     print("Sorry try again after 90 days")

# high_income = True
# good_credit = False

# if high_income and good_credit:
#     print("You are eligible for the loan")

# else:
#     print("Sorry try again after 90 days")

# high_income = True
# good_credit = False

# if high_income or good_credit:
#     print("You are eligible for the loan")

# else:
#     print("Sorry try again after 90 days")

# high_income = False
# good_credit = False

# if high_income or good_credit:
#     print("You are eligible for the loan")

# else:
#     print("Sorry try again after 90 days")


has_good_credit = True                                      # use of not operator 
has_criminal_record = True

if has_good_credit and not has_criminal_record:
    print("Eligible for the loan")
else:
    print("Uneligible for the loan")


has_good_credit = True                                      # use of not operator 
has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print("Eligible for the loan")
else:
    print("Uneligible for the loan")