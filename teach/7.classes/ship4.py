#ship4.py add a second yacht
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
yacht = Ship()
boat.getShipName()
yacht.getShipName()
print("now it gets changed")
boat.setShipName()
yacht.setShipName()
boat.getShipName()
yacht.getShipName()

