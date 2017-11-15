#maxFunc.py - max function 
#andyp - 13.09.12

def maxFunc(firstNum,secondNum):
	if firstNum > secondNum:
		larger=firstNum
	else:
		larger=secondNum
	return(larger)

firstNum=int(input('Enter the first number :'))
secondNum=int(input('Enter teh second number :'))
print ('The biggest number is ', maxFunc(firstNum,secondNum))
