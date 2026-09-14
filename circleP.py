import math
print("hello Sir, welcome to circle eara and perimeter calculator")
radius = float(input("Please enter the radius of the circle in cm : "))

result_perimeter = round((2 * math.pi * radius), 2) 
result_area = round((pow(radius, 2) * math.pi), 2)

print(f"The perimeter of the circle is: {result_perimeter}cm")
print(f"The area of the circle is: {result_area}cm²")