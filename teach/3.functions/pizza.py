#!/usr/local/bin/python3.3
#pizza.py pizza house program
#andyp 13.09.13

import pudb; pu.db

#function declaration

def printToppings(topping):
	count=0;
	while (count<len(topping)):
		print (count+1, topping[count])
		count+=1
	return()

def printSize(size):
	count=0
	print  ('Pablos Pizza Palace')
	print  ('===================')
	while(count<len(size)):
		print(count+1, size[count])
		count+=1
	#TODO input validation
	sizeOfPizza=int(input('Please pick a pizza size: '))
	print('')
	return(sizeOfPizza)

def chooseToppings(topping):
	print('Choose up to 3 toppings')
	print('=======================')
	printToppings(topping)
	print('Enter 0 for no more toppings')
	print ('')
	topChoice=int(input("Enter a valid number ")) #TODO need validation for input here and dropout on zero
	return(topChoice)

def printOrder(choice):
	choiceNum=0
	while choice[choiceNum] < 4:
		print('Your order is')
		print(printSize[choice[choiceNum]], 'pizza')
		choiceNum+=1
	return()

#variable declarations

topping=('chicken','beef','pork','ham','sweetcorn')
size=('small','medium','large')
anotherPizza=1
pizza=[0,0,0,0]
choice=[pizza*5]
pizza=[]
pizzaNum=0

#TODO needs a loop for Pizza
#TODO preload pizza data with 0?
#main loop
while anotherPizza==1:
	print('Pizza number ', pizzaNum+1)
	choice[pizzaNum]=[printSize(size),chooseToppings(topping),chooseToppings(topping),chooseToppings(topping)]
	#TODO maybe ue extend here
	print(choice[pizzaNum]) #test print
	pizzaNum+=1
	anotherPizza=int(input('Do you want another pizza 1=Yes,2=No'))

printOrder(choice)
