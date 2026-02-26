# TASK 1, 2, 3

n = int(input("Enter n: "))

for i in range(1, n + 1):
    print(i, end="")


# TASK 4

rows = 5

for i in range(rows):
    print(" " * i + "* " * (rows - i))


    # TASK 5

rows = 5

for i in range(1, rows + 1):
    print("* " * i)

# TASK 6

rows = 5

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# TASK 7: Prime Number Finder

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

num = start

print("Prime numbers between", start, "and", end, "are:")

while num <= end:
    if num > 1:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")
    num += 1