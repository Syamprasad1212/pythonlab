def interchange(lit):
	if len(lit) <2:
		return lit
	lit[0],lit[-1]=lit[-1],lit[0]
	return lit

my_list=[1,2,3,4,5,6,7]
print("original list",my_list)	
print("interchanged list:",interchange(my_list))
