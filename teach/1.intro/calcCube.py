# calcCube.py - calculates a cube and determines when area = volume
# andyp - 16.10.17

width = 1
height = 1
depth = 1
area = 0
volume = 0

for width in range(1,10):
    for depth in range(1,10):
        for height in range(1,10):
            print( "width : ", width, " depth : ", depth, " height ", height )
            volume = depth * width * height
            print("volume: ", volume)
            area = 2*((depth*width) + (depth*height) + (width*height))
            print("area: ", area) 

            if area == volume:
                print ("bingo ", width, " ", height , " ", depth, " match")
                break;
