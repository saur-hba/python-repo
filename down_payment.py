price = 1000000
good_credit = True

if good_credit:
    down_payment = 0.1 * price
    print(f"Down payment for this house is: ${down_payment}")
else:
    down_payment = 0.2 * price
    print(f"Down payment for this house is: ${down_payment}")