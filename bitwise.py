x = 10  # Binary: 1010
y = 4   # Binary: 0100

print("x & y =", x & y)  # Bitwise AND (1000 -> 8)
print("x | y =", x | y)  # Bitwise OR  (1110 -> 14)
print("x ^ y =", x ^ y)  # Bitwise XOR (1110 -> 14)
print("~x =", ~x)        # Bitwise NOT (-11, because of two's complement)
print("x << 1 =", x << 1) # Left shift (10100 -> 20)
print("x >> 1 =", x >> 1) # Right shift (0101 -> 5)

