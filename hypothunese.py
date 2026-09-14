import math
print("hello Sir,welcome to triangle calculator")
A = float(input("Please enter the length of side A in cm : "))
B = float(input("Please enter the length of side B in cm : "))
C = round(math.sqrt(pow(A, 2) + pow(B, 2)), 2)
print(f"The length of the hypotenuse C is: {C} cm")