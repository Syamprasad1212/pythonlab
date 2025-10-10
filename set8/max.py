numbers = [10, 25, 7, 98, 43, 7, 98]

min_value = min(numbers)
max_value = max(numbers)

min_position = numbers.index(min_value)  # First occurrence of min value
max_position = numbers.index(max_value)  # First occurrence of max value

print(f"Minimum value: {min_value} at position: {min_position}")
print(f"Maximum value: {max_value} at position: {max_position}")
