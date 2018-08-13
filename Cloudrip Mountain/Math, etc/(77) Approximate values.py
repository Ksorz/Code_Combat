# We must summon the Ancient Warrior for this ogre!
# Four paladins must form a rectangle.
# But the rectangle needs a specific area and perimeter
# Paladins will keep moving, say the spell when ready.
# It is hard to be precise, but almost equal is good.


# This function should compare valueA and B within 3%.
def almostEqual(valueA, valueB):
    # Check if valueA is > 0.97 and < 1.03 of valueB.
    if valueA > valueB * 0.97 and valueA < valueB * 1.03:
        # As a default, just check equality.
        return True

# The function checks the equality with 5% inaccuracy.
def almostEqual_II(a, b):
    return Math.abs(a - b) < (b * 0.05)

# This function is useful to compare float numbers.
def almostEqual_III(a, b):
    return Math.abs(a - b) < 1

# This function should calculate the perimeter:
def perimeter(side1, side2):
    # The perimeter is the sum of all four sides.
    perimeter = (side1 + side2) * 2
    return perimeter

# This function should return the area:
def area(side1, side2):
    # The area of a rectangle is the product of 2 sides
    area = side1 * side2
    return area

# Required summoning values for area and perimeter:
requiredPerimeter = 104
requiredArea = 660

# We will use this unit as a base for our calculations:
base = hero.findNearest(hero.findFriends())

while True:
    sideSN = base.distanceTo("Femae")
    sideWE = base.distanceTo("Illumina")
    currentPerimeter = perimeter(sideSN, sideWE)
    currentArea = area(sideSN, sideWE)
    if almostEqual(currentArea, requiredArea) and almostEqual(currentPerimeter, requiredPerimeter):
        hero.say("VENITE!")
        break
