#mini test 2
#andyp 13.10.13

seedVal = 0
count = 0
seedVal = int(input('Enter a number to countdown from '))
while seedVal < 0 :
    seedVal = int(input('Please Enter a number to countdown from '))

while (seedVal - count) > -1:
    print (seedVal -count)
    count += 1


