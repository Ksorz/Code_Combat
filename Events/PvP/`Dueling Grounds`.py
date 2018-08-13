enemies = hero.findEnemies()
hp = 0
for enemy in enemies:
    if enemy.health > hp:
        hp = enemy.health
        CRAB = enemy

# Settings
Center = {"x": 80, "y": 69}
rangeUnits = "shaman" and "thrower" and "fangrider" and "headhunter" and "archer"
jumpIndex = 0
jumpDis = 8
factor = 1.8
reverseFactor = factor * 2 - 1
fromCenterDis = Center.x / factor
# -------
hero.cast("fear", CRAB)

def chooseStrategy():
    if hero.canCast("poison-cloud") and enemies.length > 5 and poisonPlace():
        hero.cast("poison-cloud", poisonPlace())
    elif enemy and hero.canCast("chain-lightning", enemy):
        return "fight"
    elif hero.canCast("raise-dead") and around(hero, hero.findCorpses(), 20) >= 11:
        hero.cast("raise-dead")
    elif hero.canCast("summon-burl") or hero.canCast("summon-undead"):
        return "summon"
    elif hero.distanceTo(CRAB) < 6:
        RUN = whereToRun(hero, 12, 7)
        if RUN:
            hero.move(RUN)
        else:
            return "fight"
    else:
        return "fight"

def hazardAround(position, rad):
    hazards = hero.findHazards()
    alert = None
    closest = 99999
    for hazard in hazards:
        current = hazard.distanceTo(position)
        if current <= rad and closest > current:
            closest = current
            alert = hazard
    return alert

def whereToRun(unit, radius, step):
    runHere = None
    aX = unit.pos.x - CRAB.pos.x
    aY = unit.pos.y - CRAB.pos.y
    angle = Math.atan2(aY, aX)
    step = step / radius
    for i in range(15):
        angle -= step
        newX = CRAB.pos.x + (radius * Math.cos(angle))
        newY = CRAB.pos.y + (radius * Math.sin(angle))
        runHere = Vector(newX, newY)
        if hero.isPathClear(hero.pos, runHere) and not hazardAround(runHere, 6):
            break
    return runHere

def onSpawn(event):
    while True:
        item = hero.findNearestItem()
        if item and hero.health < hero.maxHealth / 1.3:
            pet.fetch(item)

def around(unit, units, dis):
    count = 0
    for i in range(len(units)):
        distance = unit.distanceTo(units[i])
        if distance <= dis:
            count += 1
    return count

def poisonPlace():
    maxCount = 3
    victim = None
    for enemy in enemies:
        count = around(enemy, enemies, 10) - around(enemy, friends, 10)
        if count > maxCount:
            maxCount = count
            victim = enemy
    return victim

def targetAoe(units, unitType, aoe):
    correctType = hero.findByType(unitType, units)
    target = None
    if correctType.length > 3:
        maximum = 2
        for unit in correctType:
            count = around(unit, correctType, aoe)
            if maximum < count:
                maximum = count
                target = unit
    return target

def minionTarget(enemies, enemyType, friend, rad):
    closest = None
    closestDis = 9999
    for enemy in enemies:
        distance = friend.distanceTo(enemy)
        if distance <= rad and distance < closestDis:
            closest = enemy
            closestDis = distance
    return closest

def summon():
    if hero.gold >= hero.costOf("soldier"):
        hero.summon("soldier")
    elif hero.canCast("summon-burl"):
        hero.cast("summon-burl")
    elif hero.canCast("summon-undead"):
        hero.cast("summon-undead")

def command():
    friends = hero.findByType("skeleton" and "soldier", hero.findFriends())
    for friend in friends:
        minionTarg = minionTarget(enemies, rangeUnits, friend, 6)
        if minionTarg:
            hero.command(friend, "attack", minionTarg)
        else:
            hero.command(friend, "attack", friend.findNearest(enemies))

def fight():
    if enemy:
        rangeEnemies = targetAoe(enemies, rangeUnits, 4)
        if hero.isReady("devour") and hero.distanceTo(enemy) < 6 and enemy.health > 170:
            hero.devour(enemy)
        elif hero.canCast("chain-lightning", enemy):
            hero.cast("chain-lightning", enemy)
        elif hero.health < 1500 and hero.canCast("drain-life", enemy):
            hero.cast("drain-life", enemy)
        elif rangeEnemies:
            hero.attack(rangeEnemies)
        else:
            hero.attack(enemy)

pet.on("spawn", onSpawn)

while True:
    if hero.canCast("fear", CRAB):
        hero.cast("fear", CRAB)
    enemies = hero.findEnemies()
    enemy = hero.findNearestEnemy()
    friends = hero.findFriends()
    if friends:
        command()
    strategy = chooseStrategy()
    if strategy == "fight":
        fight()
    elif strategy == "summon":
        summon()
