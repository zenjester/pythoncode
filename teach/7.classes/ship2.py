#ship2.py intro to clasess
#andyp 13.10.13

class Ship:
    name = "Titanic"
    type = "liner"
    speed =0
    direction=180

    def getShipName(self):
        print(self.name)
        return

boat = Ship()
boat.getShipName()

