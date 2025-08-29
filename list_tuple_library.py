
# I. Find length of tuple without len()
t = (1, 2, 3, 4)
count = 0
for _ in t:
    count += 1
print("Length of tuple:", count)

# II. Max & Min of a tuple
numbers = (5, 2, 9, 1)
print("Max:", max(numbers))
print("Min:", min(numbers))

# III. Remove duplicates from a list
lst = [1, 2, 2, 3, 4, 4]
lst = list(set(lst))
print("No duplicates:", lst)

# IV. Square each element in list
nums = [1, 2, 3, 4, 5]
squares = [x**2 for x in nums]
print("Squares:", squares)

# V. Merge two dictionaries
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3}
merged = {d1, d2}
print("Merged dictionary:", merged)

# VI. Swap keys and values
d = {'a': 1, 'b': 2, 'c': 3}
swapped = {v: k for k, v in d.items()}
print(swapped)

# VII. Fibonacci with memoization
def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
print("Fibonacci(10):", fib(10))

# VIII. Pythagorean triplets up to n
n = 20
triplets = [(a, b, c) for a in range(1, n)
            for b in range(a, n)
            for c in range(b, n)
            if a*a + b*b == c*c]
print("Triplets:", triplets)

# IX. Shopping cart with nested dict
cart = {}
cart["apple"] = {"price": 2, "qty": 3}
cart["banana"] = {"price": 1, "qty": 5}
total = sum(item["price"] * item["qty"] for item in cart.values())
print("Total:", total)

# X. Dictionary-based cache (LRU)
from collections import OrderedDict
class LRUCache:
    def init(self, max_size):
        self.cache = OrderedDict()
        self.max_size = max_size
    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return None
    def put(self, key, value):
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.max_size:
            self.cache.popitem(last=False)

# XI. Even numbers from tuple
nums = (1, 2, 3, 4, 6)
even_nums = tuple(x for x in nums if x % 2 == 0)
print("Even numbers:", even_nums)

# XII. Sort list of tuples by second element
pairs = [('a', 3), ('b', 1)]
pairs.sort(key=lambda x: x[1])
print(pairs)

# XIII. Flatten nested list
nested = [[1, 2], [3, 4]]
flat = [x for sub in nested for x in sub]
print(flat)

# XIV. Remove all occurrences of an element
lst = [1, 2, 3, 2, 4]
element = 2
lst = [x for x in lst if x != element]
print(lst)

# XV. Invert dictionary (handle duplicate values)
d = {'a': 1, 'b': 1, 'c': 2}
inv = {}
for k, v in d.items():
    inv.setdefault(v, []).append(k)
print(inv)

# XVI. Student with highest average
marks = {
    "John": [90, 80, 85],
    "Jane": [95, 92, 88],
    "Bob": [70, 75, 80]
}
highest = max(marks, key=lambda name: sum(marks[name]) / len(marks[name]))
print("Top student:", highest)