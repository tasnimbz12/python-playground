print("Welcome to the Temperature Conversion Program!")
unit = input("Please enter the unit you want to convert from (C, F): ").upper()
temperature = float(input("Please enter the temperature value: "))
if unit == "C":
    result = (temperature * 9/5) + 32
    print(f"{temperature}°C is equal to {result}°F")
elif unit == "F":
    result = (temperature - 32) * 5/9
    print(f"{temperature}°F is equal to {result}°C")
else:
    print("Invalid unit. Please enter either 'C' or 'F'.")