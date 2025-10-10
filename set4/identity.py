a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("a is b:", a is b)  # True, both refer to same object
print("a is c:", a is c)  # False, different objects with same content
print("a == c:", a == c)  # True, values/content are equal

print("a is not c:", a is not c)  # True
