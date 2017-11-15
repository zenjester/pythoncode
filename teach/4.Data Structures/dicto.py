#dicto.py a dictionary example
#andyp 13.01.13

empNumber = {'Bob' : 1, 'Guido' : 3, 'James' : 7}
print(empNumber['Guido'])
empNumber['nick']=8
print(empNumber)
if (empNumber['bob']):
    print ('Hello bob')
else:
    print ('bob does not exist')
findNum=input()
print(empNumber[findNum])

