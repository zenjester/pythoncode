#mesSages.py - various messaging strings
#andyp - 11.03.11

msg1 = "All it takes for evil to flourish is for good men to remain silent"

if not(msg1.startswith("Pickle")):
    print("Doesn't start with pickle")
else:
    print("Starts with Pickle")

msg2 = "filename.txt"

if msg2.endswith(".txt"):
	print ("Text file")
else:
	print("Not a text file")

print(msg2.upper())
print(msg2.lower())

msg3=msg2.replace(".txt",".doc")

if msg3.endswith(".txt"):
	print ("Text file")
else:
	print("\"Not a text file\"")

print(msg1.find("for"))
