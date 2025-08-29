
# 1) Print numbers from 1 to 10 using for loop
for i in range(1, 11):
    print(i)

# 2) Multiplication table using while loop
num = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1

# 3) Pyramid pattern
n = int(input("Enter height: "))
for i in range(1, n + 1):
    print("*" * i)

# 4) Prime numbers up to a given number
limit = int(input("Enter limit: "))
for num in range(2, limit + 1):
    is_prime = True
    for j in range(2, int(num**0.5) + 1):
        if num % j == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
print()

# 5) Recursive factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
print("Factorial(5):", factorial(5))

# 6) Function sum of any number of args
def sum_all(*args):
    return sum(args)
print("Sum:", sum_all(1, 2, 3, 4))

# 7) Skip number 5 using continue
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# 8) Stop loop at number 7 using break
for i in range(1, 11):
    if i == 7:
        break
    print(i)

# 9) Tower of Hanoi
def hanoi(n, source, target, aux):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n-1, source, aux, target)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n-1, aux, target, source)
hanoi(3, 'A', 'C', 'B')

# 10) Simple Tic-Tac-Toe simulation
board = [" "]*9
player = "X"
for turn in range(9):
    pos = int(input(f"Player {player}, choose position (0-8): "))
    if board[pos] == " ":
        board[pos] = player
    else:
        print("Position taken, try again.")
        continue
    print(board[0:3])
    print(board[3:6])
    print(board[6:9])
    if (board[0] == board[1] == board[2] != " " or
        board[3] == board[4] == board[5] != " " or
        board[6] == board[7] == board[8] != " " or
        board[0] == board[3] == board[6] != " " or
        board[1] == board[4] == board[7] != " " or
        board[2] == board[5] == board[8] != " " or
        board[0] == board[4] == board[8] != " " or
        board[2] == board[4] == board[6] != " "):
        print(f"Player {player} wins!")
        break
    player = "O" if player == "X" else "X"