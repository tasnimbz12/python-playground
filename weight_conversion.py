print(" Welcome to the Weight Conversion Program!")
unit = input("Please enter the unit you want to convert from (kg, lb): ").lower()
weight = float(input("Please enter the weight you want to convert: "))
if unit == "kg" or unit == "kilogram ":
    result = round((weight * 2.20462), 2)
    print(f"{weight} kg is equal to {result} lb.")
elif unit == "lb" or unit == "pound":
    result = round((weight / 2.20462), 2)
    print(f"{weight} lb is equal to {result} kg.")
else:

    print("Invalid unit. Please enter either 'kg' or 'lb'.")

