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
a = float(input("Side a: "))
b = float(input("Side b: "))
c = float(input("Side c: "))
if a + b > c and a + c > b and b + c > a:
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print(f"Area: {area:.2f}")
# 4. Create a program that computes different statistics given five numbers including the total, average, minimum, maximum, range, and standard deviation (https://en.wikipedia.org/wiki/Standard_deviation).
import math
nums = [float(input(f"Enter number {i + 1}: ")) for i in range(5)]
total = sum(nums)
avg = total / 5
std_dev = math.sqrt(sum((x - avg) ** 2 for x in nums) / 5)
print("\nStatistics:")
print(f"Total: {total}")
print(f"Average: {avg:.2f}")
print(f"Minimum: {min(nums)}")
print(f"Maximum: {max(nums)}")
print(f"Range: {max(nums) - min(nums)}")
print(f"Standard Deviation: {std_dev:.2f}")
