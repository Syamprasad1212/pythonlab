f=open("binary.bin",'wb')
f.write(b'\x00\x01\x02\x03\x04')
f=open('binary.bin','rb')
print(f.read())
