import csv
f=open('table.csv','r')
rf=csv.reader(f)
for row in rf:
	print(row)
