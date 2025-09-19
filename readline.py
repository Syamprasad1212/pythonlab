#used readline and readlines to print file content
ff=open("demoo.txt",'r')
print(ff.readline())
print("readline is done")
print(ff.readlines())
print("read using readlines")
ff.close()
