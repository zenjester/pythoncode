# prime number calculator
#andyp 27.06.14
#primeNum2.py

candidates = []
candidates.extend(range(2, 1000))


def primeCalc(candidates, denom):
    x = 0

    while x < len(candidates):
        if (((candidates[x] % denom) == 0) and (candidates[x] != denom)):
            candidates.remove(candidates[x])
        x += 1
    return

denom = 2

while denom < (len(candidates) + 1):
    primeCalc(candidates, denom)
    denom += 1

print(candidates)
