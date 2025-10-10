a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("The triangle is valid.")
else:
    print("The triangle is NOT valid.")
