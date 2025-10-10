# Create and write to file
with open("example.txt", "w") as file:
    file.write("Hello, this is the first line.\n")
    file.write("This is the second line.")

# Read from the file
with open("example.txt", "r") as file:
    content = file.read()

print("Content of the file:")
print(content)
