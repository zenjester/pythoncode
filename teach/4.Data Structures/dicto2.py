#dicto2.py a dictionary example

print(empNumber['Guido'])
empNumber['nick']=8
print(empNumber)
if 'bob' in empNumber:
    print (empNumber['bob'])
else:
    print ('bob does not exist')
findNum=input()
print(empNumber[findNum])
