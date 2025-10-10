# Writing to a binary file
data = b"Hello, this is binary data!"  # b'' denotes bytes literal

with open("binaryfile.bin", "wb") as file:  # 'wb' = write binary
    file.write(data)

# Reading from a binary file
with open("binaryfile.bin", "rb") as file:  # 'rb' = read binary
    content = file.read()

print("Binary file content:", content)

