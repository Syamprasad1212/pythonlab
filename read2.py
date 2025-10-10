f="sample.txt"
with open(f,"w")as s:
	s.write("Hi from syam")
	s.write("How are u")

with open(f,"r")as s:
	content=s.read()
print("content is:")
print(content)
