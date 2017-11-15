#tuples.py shows tuples in action
#andyp 13.1.12

def printme():
	tup = ('first','second', 'third')
	for n in range(3):
		print ('the ', tup[n], 'is' , n)
	return()

printme()