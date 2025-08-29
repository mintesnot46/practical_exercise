
# 1. Function to return square of a number
def square(num):
    return num ** 2
print("Square of 5:", square(5))

# 2. Palindrome check
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
print("Is 'madam' palindrome?", is_palindrome("madam"))

# 3. Decorator to log execution time
import time
def log_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.6f} seconds")
        return result
    return wrapper

@log_time
def slow_function():
    time.sleep(1)
    print("Finished slow function")
slow_function()

# 4. Generator for infinite prime numbers
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_generator():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

primes = prime_generator()
for _ in range(10):  # print first 10 primes
    print(next(primes), end=" ")
print()