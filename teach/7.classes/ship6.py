#ship6.py multiple  objects and all methods correct
#andyp 13.10.13

class Ship:
    def __init__(self,shipNum,name,shipType,speed,direction):
	    self.shipNum = shipNum
	    self.name = name
	    self.shipType = shipType
	    self.speed = speed
	    self.direction = direction

    def getShipName():
        print(name)
        return

    def setShipName(self):
        self.name = input("Input the Ships Name \n")
        return

    def setShipType(self):
        sType = ('liner', 'barge', 'yacht', 'warship')
        inType = ' '
        while inType not in sType:
            inType = input('Enter a valid ship type')
        return

    def setShipSpeed(self):
        self.name = int(input('Enter the ship speed '))
        return


    def getShipData(self):
        print ('Ship Name is ', self.name)
        return


    def getShipSpeed(self):
        print('Ship Speed is ', self.speed)
        return


    def getShipName(self):
        print('Ship Name is ')
        return

boat = Ship(17,'titanic','liner',10,20)
boat.getShipName()
yacht = Ship(12,'blossom','yacht',10,210)
yacht.getShipName()
print("now it gets changed")
boat.setShipName()
boat.getShipName()
yacht.setShipName()
yacht.getShipName()
yacht.setShipType()
yacht.setShipSpeed()
yacht.getShipData()
#ships =[Ship(i," "," ",0,0)
