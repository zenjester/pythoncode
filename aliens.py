# aliens.py - test concept program
# Andyp 08.09.17

alien_0 = {'color': 'green', 'points': 5}
newpoints = alien_0['points']
print("You just earned " + str(newpoints) + " points!")
alien_0['xposition'] = 0
alien_0['yposition'] = 25
print("the alien is " + alien_0['color'] + ".")
alien_0["color"] = 'yellow'
print("the alien is now " + alien_0['color'] + ".")
