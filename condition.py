# 1. Check if a number is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 2. Find the largest of three numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)

# 3. Categorize age
age = int(input("Enter your age: "))
if age < 13:
    print("Child")
elif age <= 19:
    print("Teen")
else:
    print("Adult")

# 4. Triangle type
a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))
if a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")
