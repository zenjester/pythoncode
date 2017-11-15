#ship3.py add getters and setters
#andyp 13.10.13

class Ship:
    name = "Titanic"
    shipType = "liner"
    speed =0
    direction=180

    def getShipName(self):
        print(self.name)
        return

    def setShipName(self):
        self.name = input("Input the Ships Name \n")
        return


boat = Ship()
boat.getShipName()
print("now it gets changed")
boat.setShipName()
boat.getShipName()

