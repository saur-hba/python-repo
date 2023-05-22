temp = float(input("Enter temperature: "))
unit = input("(C)elsius or (F)arenheit: ")
if unit.upper() == "C":
    converted = (temp * 9/5) + 32
    print("Converted temp into farehneit is ", converted)
else:
    converted = (temp - 32) *5/9
    print("Converted temp into celsius is ", converted)


# def fahrenheit_to_celsius(fahrenheit):
#     celsius = (fahrenheit - 32 ) * 5/9
#     return celsius
# def celsius_to_fahrenheit(celsius):
#     fahrenheit = (celsius * 9/5) + 32
#     return fahrenheit

# temperature_in_fahrenheit = float(input("Enter temperature in fahrenheit: "))
# print(f"Converted temperature in celsius is " ,fahrenheit_to_celsius(temperature_in_fahrenheit))

# temperature_in_celsius = float(input("Enter temperature in celsius: "))
# print(f"Converted temperature in fahrenheit is",celsius_to_fahrenheit(temperature_in_celsius))
