# 1. Create a program that prints the following output to the screen: "Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked."
print ("Water Earth, Fire, Air. Long ago, the four nations lived together in harmony. Then, everything changed when the fire nation attacked.")
# 2. Create a program that prompts for 2 numbers and then outputs the addition, subtraction, multiplication, and division of the first number by the second number.
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
print (f"\nresults:")
print(f"Addition: {num1} + {num2} = {num1 + num2}")
print(f"Subtraction: {num1} - {num2} = {num1 - num2}")
print(f"Multiplication: {num1} * {num2} = {num1 * num2}")
print(f"Division: {num1} / {num2} = {num1 / num2 if num2 != 0 else 'Undefined (division by zero is not allowed)'}")
# 3. Create a program that prompts for the side lengths of a triangle and computes the area using Heron's formula. (https://en.wikipedia.org/wiki/Heron%27s_formula)
import math 
a = float(input("Side a: "))
b = float(input("Side b: "))
c = float(input("Side c: "))
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print(f"The area of the triangle is: {area:.2f} square units.")

# 4. Create a program that computes different statistics given five numbers including the total, average, minimum, maximum, range, and standard deviation (https://en.wikipedia.org/wiki/Standard_deviation).
import math

a = float(input("Enter number 1: "))
b = float(input("Enter number 2: "))
c = float(input("Enter number 3: "))
d = float(input("Enter number 4: "))
e = float(input("Enter number 5: "))

total = a + b + c + d + e
average = total / 5
minimum = min(a, b, c, d, e)
maximum = max(a, b, c, d, e)
range_value = maximum - minimum
variance = ((a - average) ** 2 + (b - average) ** 2 + (c - average) ** 2 + (d - average) ** 2 + (e - average) ** 2) / 5
standard_deviation = math.sqrt(variance)

print(f"Total: {total}")
print(f"Average: {average:.2f}")
print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")
print(f"Range: {range_value}")
print(f"Standard Deviation: {standard_deviation:.2f}")
