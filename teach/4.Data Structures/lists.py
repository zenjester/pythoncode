#lists.py - showing python lists
#andyp - 13.01.12

def printFood(count):
	n=0
	while (n < count):
		print (n, food[n])
		n=n+1;
	return()
	
def foodChoice():
	
	print('you have chosen a', food[3])
	print ('oops bad spelling')
	food[3]='Kebab'
	print('you have chosen a', food[3])
	print ('lets add some heathly options')
	food.append ('salads')
	print('')
	printFood(5)
	cakes = ['eclair', 'sponge', 'lemon drizzle']
	food.extend(cakes)
	print('')
	print('add cakes')
	printFood(len(food))
	print('')
	print('in reverse')
	food.reverse()
	printFood(len(food))
	print('')	
	print('it\'s sorted rodney')
	printFood(len(food))
	return()

food =['pizza','chips','burger','kebabb']	
foodChoice()
	