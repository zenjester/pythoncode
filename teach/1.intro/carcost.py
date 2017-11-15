# car pricing program carCost.py
miles = float(input('Enter the number of miles travelled :'))
mpg = float(input('Enter your miles per gallon :'))
costPerGallon= float(input('Enter the cost per gallon :'))
parkCost = float(input('Enter your daily parking costs :'))
tax = float(input('Enter your Road Tax'))
service = float(input('Enter annual service cost'))
insurance = float(input('Enter annual insurance cost'))

totalCost=(parkCost+((miles/mpg)*costPerGallon * 221)) + tax + service + insurance

print ('total journey cost is ' + str(totalCost))
