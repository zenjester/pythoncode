#strReverse.py reverses a string
#andyp 12.09.12

def strReverse(inStr):
	strlen=len(inStr)
	count=0
	newStr=''
	while (count != strlen):
		newStr=newStr+inStr(strlen-count)
		count=count+1
	return(newStr)

print(strReverse('nest in lif'))

