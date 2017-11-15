#prime number calculator
#andyp 27.06.14

def primeCalc(candidate):
	denom=2
	while (denom <99):
		if ((candidate%denom) == 0):
			prime= 'not a'
			break
		else:
			prime= 'is a prime'
			break
		denom+=1
	return(prime)	
nums=range(2,100)
for candidate in nums:
	print(candidate,primeCalc(candidate))
