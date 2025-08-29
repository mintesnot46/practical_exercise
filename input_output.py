# 1. Ask user name and age, then print message
name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"Hello {name}, you are {age} years old.")

# 2. Take two numbers and print their sum
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Sum =", num1 + num2)

# 3. Read a file and count words
filename = input("Enter file name: ")
with open(filename, 'r') as f:
    words = f.read().split()
print("Number of words:", len(words))

# 4. Take a sentence and write it reversed into a file
sentence = input("Enter a sentence: ")
with open("reversed.txt", "w") as f:
    f.write(sentence[::-1])
print("Sentence reversed and saved to reversed.txt")

# 5. Read CSV file and convert to dictionary
import csv
filename = input("Enter CSV file name: ")
with open(filename, newline='') as f:
    reader = csv.DictReader(f)
    data = list(reader)
print("CSV data as dictionary list:", data)

# 6. Monitor log file for a keyword
import time
log_file = input("Enter log file name: ")
keyword = input("Enter keyword to monitor: ")
with open(log_file, 'r') as f:
    f.seek(0, 2)  # Go to end of file
    while True:
        line = f.readline()
        if keyword in line:
            print("Keyword found:", line.strip())
        time.sleep(1)
