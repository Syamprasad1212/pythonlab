# python program to implement multiple inheritance
class Syam:
	def mm(self):
		print("Class 1")
		
class Ajay(Syam):
	def m(self):
		print("Class 2")

class Ram(Syam):
	def m(self):
		print("Class 3")

obj=Ram()
obj.m()
obj.mm()
