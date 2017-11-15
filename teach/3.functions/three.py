def three_func(one,two,three):
	if (one > two) and (one > three) :
		large=one
	elif (two > one) and (two > three) :
		large=two
	else:
		large=three
	return (large)

print('enter your numbers :')
one=int(input('first number :'))
two=int(input('second number : '))
three=int(input('three number :' ))
print('the biggest number is',three_func(one,two,three))


		
