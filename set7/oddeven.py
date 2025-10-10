numbers = [10, 23, 45, 66, 77, 84, 90]

even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
