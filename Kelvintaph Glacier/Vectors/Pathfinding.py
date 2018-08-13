# Say anything within 10m of Omarn for him to throw a potion.
# Catch the potion by standing near it before it lands.
# DO NOT LET THE POTION LAND ON THE GROUND!
hazards = hero.findHazards()
startPos = Vector(14, 34)
def _angle_(start, end):
    return Vector.heading(Vector.subtract(end, start))

def moving(array):
    for i in array:
        hero.move(i)

def isAlert(point, dist):
    for hazard in hazards:
        if Vector.distance(point, hazard.pos) <= dist:
            return hazard

def path(start, end):
    A_end = []
    A = start
    previous = A
    while Vector.distance(A, end) > 1.5:
        path = Vector.subtract(end, A)
        path = Vector.normalize(path)
        path = Vector.multiply(path, 1.5)
        path = Vector.add(A, path)
        if isAlert(path, 4):
            mine = isAlert(path, 4)
            angle = _angle_(mine.pos, path)
            if _angle_(path, end) > _angle_(mine.pos, end):
                angle += 0.5
            else:
                angle -= 0.5
            X = mine.pos.x + (4.5 * Math.cos(angle))
            Y = mine.pos.y + (4.5 * Math.sin(angle))
            path = Vector(X, Y)
        A_end.append(path)
        A = path
    return A_end

while True:
    potion = hero.findFriendlyMissiles()[0]
    # Remember that a Fire Trap will trigger if you move closer than 3 meters!
    omarn = hero.findByType("potion-master")[0]
    if potion:
        dest = potion.targetPos;
        # Go get the potion.
        A_end = path(hero.pos, dest)
        moving(A_end)
        pass
    else:
        if omarn and hero.distanceTo(omarn) > 10:
            # Move back to Omarn.
            A_end = path(hero.pos, startPos)
            moving(A_end)
            # Warning: isPathClear doesn't work with Hazards!
            pass
        else:
            hero.say("Hup, hup!")
