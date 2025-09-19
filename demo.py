#reading from a file direct from program using file modes
fr=open('demo.txt','r')
print(fr.read())
print('reading is done')
fr.close()
