#program to implement Destructor
class Destructor:
	def __init__(self):
		print("object created")
	
	def __del__(self):
		print("Destructor called")
obj=Destructor()
del obj
