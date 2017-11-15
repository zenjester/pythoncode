# hammi a hammubrai clone
# andyp 20.10.14

import random
# initialise locals

chance = 0
year = 2
population = 95
starved = 0
storage = 2800
harvest = 3000
eaten = 0
yval  = 3
acres = 1000
immigrants = 5
land_cost = 17
acres_to_buy = 0
acres_to_sell = 0
bflag = 0

while (year< 10):
	print ("in the year ", year)
	#rest of print statement
	++year
	++population
	land_cost=land_cost+random.randint(0,10)
	#buy loop
	print ("do you wish to buy some land it is trading at ", land_cost," bushells per acre")
	acres_to_buy=input ("enter number fo acres to buy or 0 for none")

test = random.randomint(1,6)

print ("test looks like", test)
