import csv
data=[
['S.no','name','Roll no'],
[1,'syam','25pa5a0536'],
[2,'ram','25pa5a0539'],
[3,'subba','25pa5a0540']]
f=open('table.csv','w',newline='')
fp=csv.writer(f)
fp.writerows(data)
