def gdg(a,b):
	a,b=abs(a),abs(b)
	if(b==0):
		return a
	return gdg(b,a%b)
print(gdg(48,18))
