x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print(f"Before swapping: x = {x}, y = {y}")

# Swapping without temp variable
x = x + y
y = x - y
x = x - y

print(f"After swapping: x = {x}, y = {y}")
