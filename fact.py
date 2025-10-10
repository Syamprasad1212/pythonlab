def factorial(num):
	if num==0 or num==1:
		return 1
	else:
		return num*factorial(num -1)

n=int(input("enter n value"))
if(n<0):
	print("-ve numbers dont have factorials")
else:
	print(f"fact {n} = {factorial(n)}") 
