#program to implement Multilevel inehritance
class Anusurya:
	def m(self):
		print("Class 1")
class Veeranjaneyulu(Anusurya):
	def mm(self):
		print("Class 2")
class Syam(Veeranjaneyulu):
	def mmm(self):
		print("Class 3")

obj=Syam()
obj.m()
obj.mm()
obj.mmm()
