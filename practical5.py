# Lab Assignment 1

# Input integers from user
numbers = tuple(map(int, input("Enter integers separated by space: ").split()))

# a) Total number of items
print("Total number of items:", len(numbers))

# b) Last item in the tuple
print("Last item:", numbers[-1])

# c) Tuple elements in reverse order
print("Tuple in reverse order:", numbers[::-1])

# d) Check if tuple contains integer 5
if 5 in numbers:
    print("Tuple contains 5")
else:
    print("Tuple does not contain 5")

# e) Remove first and last items
if len(numbers) > 2:
    new_tuple = numbers[1:-1]
else:
    new_tuple = ()

print("Tuple after removing first and last items:", new_tuple)

# Lab Assignment 2

# Input prices
prices = tuple(map(float, input("Enter prices of sold items: ").split()))

# a) Total number of items sold
print("Total items sold:", len(prices))

# b) Cheapest item price
print("Cheapest item price:", min(prices))

# c) Costliest item price
print("Costliest item price:", max(prices))

# d) Prices in ascending order
print("Prices in ascending order:", tuple(sorted(prices)))

# e) Number of costliest items sold
costliest_count = prices.count(max(prices))
print("Number of costliest items sold:", costliest_count)