#!/usr/local/bin/python3.3
a, b = 0, 1
while b < 1000000:
    print (b)
    a, b = b, a + b
