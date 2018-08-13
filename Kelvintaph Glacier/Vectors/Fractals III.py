# You are on your own this time, I hope you have learned what you need from the previous fractal levels. Check the guide for help with what you need to do and with the math required for polygons.
yaks = hero.findEnemies()

# You need a function to convert degrees to radians.  Multiply degrees by Math.PI / 180.
def degToRad(deg):
    return deg * (Math.PI / 180)

# Your polygon function should have 3 inputs: start, end, and sides.
def polygon(A, B, side):
    # Remember to make your polygon recursive, drawing extra polygons at every corner.
    hero.toggleFlowers(False)
    start = A
    end = B
    full = Vector.subtract(end, start)
    distance = full.magnitude()
    hero.moveXY(start.x, start.y)
    hero.toggleFlowers(True)
    for i in range(side):
        hero.moveXY(end.x, end.y)
        full = Vector.rotate(full, degToRad(360 / side))
        if distance > 7:
            polygon(end, Vector.add(end, Vector.divide(full, 5)), side)
        end = Vector.add(end, full)

# To get the start and end position for each polygon, add startOffset and endOffset to the yak's position.

startOffset = Vector(-15, -15)
endOffset = Vector(15, -15)

# You need to loop through all the yaks, drawing a polygon for each.  Yaks are enemies.
for yak in yaks:
    start = Vector.add(yak.pos, startOffset)
    end = Vector.add(yak.pos, endOffset)
    sides = yak.sides
    polygon(start, end, sides)
