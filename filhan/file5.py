with open("j.txt",'w+') as f :
	f.write('i m patel')
	f.seek(0)
	print(f.read())

print('done')
