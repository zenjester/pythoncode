#variables.py - use of variables
#andyp - 

lint=12
floater=3.14
vest="much muppetry"

print (lint,floater, vest)

lint = lint/5
floater=floater * 3
vest = vest + " in bash"

print (lint,floater, vest)

smallLint=lint
oldFloater=floater
lint=lint * 100
floater = int(floater/6)
vest = vest + " " + str(smallLint) + str(oldFloater)

print (lint,floater, vest)

print ("Octal %o" %lint ,"Float %.3f" %floater)
print ("Hex %x" %lint, "Octal %o" %lint)


