u# 1. Reverse a string
text = input("Enter a string: ")
print("Reversed:", text[::-1])

# 2. Count vowels in a string
string = input("Enter text: ")
vowels = "aeiouAEIOU"
count = sum(1 for ch in string if ch in vowels)
print("Number of vowels:", count)

# 3. Check if two strings are anagrams
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
if sorted(s1) == sorted(s2):
    print("They are anagrams")
else:
    print("Not anagrams")

# 4. Count word occurrences in a sentence
sentence = input("Enter a sentence: ").split()
word_count = {}
for word in sentence:
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)

# 5. Caesar Cipher (shift letters by n)
text = input("Enter text: ")
shift = int(input("Enter shift: "))
result = ""
for char in text:
    if char.isalpha():
        start = ord('A') if char.isupper() else ord('a')
        result += chr((ord(char) - start + shift) % 26 + start)
    else:
        result += char
print("Ciphered text:", result)

# 6. Validate email using regex
import re
email = input("Enter email: ")
pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
if re.match(pattern, email):
    print("Valid email")
else:
    print("Invalid email")
