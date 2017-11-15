#guess.py - updated guess program
import random

guessesTaken = 0

print( ' what is your name ?')
myName= input()

number = random.randint(1,20)
print (' so ' + myName + ', I am thinking of a number between 1 and 20')

while guessesTaken < 6:
	print('Want to enter a guess ?')
	guess = input()
	guess = int(guess)
	
	guessesTaken = guessesTaken + 1
	
	if guess < number:
		print('Your guess is too low')
		
	if guess > number:
		print ('Your guess  is too high')
		
	if guess == number:
		break
		
if guess == number:
	guessesTaken=str(guessesTaken)
	print ('Well done ' + myName + ' you guessed the correct number in ' + guessesTaken + ' guesses!')
	
if guess != number:
	number = str(number)
	print('Nope. The number i was thinking of was  ' + number)
