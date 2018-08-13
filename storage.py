vector = Vector.subtract(end, start)
vector = Vector.add(start, vector)
vector = Vector.normalize(vector)
vector = Vector.multiply(vector, 30)


for i in range(mimimi):
    hero.say(vector.magnitude())
    hero.say(vector)

    hero.toggleFlowers(False)
    hero.moveXY(start.x, start.y)
    hero.toggleFlowers(True)
    hero.moveXY(vector.x, vector.y)

    start = vector
    vector = Vector.rotate(vector, degreesToRadians(10))


















# -----------------------------------------------------------------------------
hero.setFlowerColor("red")
hero.toggleFlowers(False)
mapCenter = Vector(80, 70)
lenY = 70
lenX = 110
ratioXY = lenX / lenY
pet.moveXY(hero.pos.x, hero.pos.y)
pet.moveXY(115, 59)
rad = pet.pos
hero.wait(2)
radius = hero.distanceTo(pet)

def enemyAround(position, rad):
    if pet.distanceTo(position) <= rad:
        return True
    else:
        return False

def whereToRun(x, y, radius, step):
    aX = hero.pos.x - mapCenter.x
    aY = hero.pos.y - mapCenter.y
    angle = Math.atan2(aY, aX)
    forVec = step * 2
    step = step / radius
    angle -= step
    hero.toggleFlowers(True)
    newX = mapCenter.x + (radius * Math.cos(angle))
    newY = mapCenter.y + (radius * Math.sin(angle))
    runHere = Vector(newX, newY)
    vector = Vector.subtract(runHere, hero.pos)
    vector = Vector.normalize(vector)
    vector = Vector.multiply(vector, 2)
    runHere = Vector.add(runHere, vector)
    if enemyAround(runHere, forVec):
        while enemyAround(runHere, forVec):
            vector = Vector.subtract(mapCenter, pet.pos)
            vector = Vector.normalize(vector)
            petRad = pet.distanceTo(mapCenter)
            if petRad <= radius:
                vector = Vector.multiply(vector, forVec + radius - petRad)
            else:
                vector = Vector.multiply(vector, forVec - (petRad - radius))
            runHere = Vector.add(runHere, vector)
    hero.move(runHere)
    hero.toggleFlowers(False)

def onSpawn(event):
    while True:
        flag = hero.findFlag()
        if flag:
            pet.moveXY(flag.pos.x, flag.pos.y)
        if flag and pet.distanceTo(flag) < 3:
            hero.removeFlag(flag)

pet.on("spawn", onSpawn)

while True:
    if hero.distanceTo(pet) < 5:
        whereToRun(mapCenter.x, mapCenter.y, radius, 3)
    # -----------------------------------------------------------------------------
