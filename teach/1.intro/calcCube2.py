# calcCube.py - calculates a cube and determines when area = volume
# the cube version
# andyp - 16.10.17

edge = 1
area = 0
volume = 0

for edge in range(1, 10):
    print("edge : ", edge)
    volume = edge * edge * edge
    print("volume: ", volume)
    area = 6 * edge * edge
    print("area: ", area)
    if area == volume:
        print ("bingo ", edge, "is a match")
