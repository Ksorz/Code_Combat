Center = {"x": 60, "y": 52}
rangeUnits = "shaman" and "thrower" and "fangrider"

# Settings
jumpIndex = 0
jumpDis = 10
factor = 1.7
reverseFactor = factor * 2 - 1
fromCenterDis = Center.x / factor
#----------

def chooseStrategy():
    if hero.canCast("poison-cloud") and enemies.length > 13 and poisonPlace():
        hero.cast("poison-cloud", poisonPlace())
    elif enemy and hero.canCast("chain-lightning", enemy):
        return "fight"
    elif hero.canCast("raise-dead") and around(hero, hero.findCorpses(), 20) >= 13:
        hero.cast("raise-dead")
    elif hero.canCast("summon-burl") or hero.canCast("summon-undead"):
        return "summon"
    else:
        return "fight"

def around(unit, units, dis):
    count = 0
    for i in range(len(units)):
        distance = unit.distanceTo(units[i])
        if distance <= dis:
            count += 1
    return count

def poisonPlace():
    maxCount = 10
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
    friends = hero.findByType("skeleton" and "soldier")
    for friend in friends:
        minionTarg = minionTarget(enemies, rangeUnits, friend, 6)
        if minionTarg:
            hero.command(friend, "attack", minionTarg)
        else:
            hero.command(friend, "attack", friend.findNearest(enemies))

def fight():
    if enemy:
        rangeEnemies = targetAoe(enemies, rangeUnits, 4)
        if hero.isReady("devour") and hero.distanceTo(enemy) < 15 and enemy.health > 170:
            hero.devour(enemy)
        elif hero.canCast("chain-lightning", enemy):
            hero.cast("chain-lightning", enemy)
        elif hero.health < 1000 and hero.canCast("drain-life", enemy):
            hero.cast("drain-life", enemy)
        elif rangeEnemies:
            hero.attack(rangeEnemies)
        else:
            hero.attack(enemy)

while True:
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
    if jumpIndex % 15 == 0 and hero.pos.x <= Center.x and hero.pos.x > fromCenterDis:
        if hero.pos.y > Center.y + jumpDis:
            hero.jumpTo({"x": hero.pos.x - jumpDis,"y": hero.pos.y - (hero.pos.y - Center.y)})
        elif hero.pos.y < Center.y - jumpDis:
            hero.jumpTo({"x": hero.pos.x - jumpDis,"y": hero.pos.y + (Center.y - hero.pos.y)})
        else:
            hero.jumpTo({"x": hero.pos.x - jumpDis,"y": hero.pos.y})
    elif jumpIndex % 15 == 0 and hero.pos.x > Center.x and hero.pos.x < reverseFactor * fromCenterDis:
        if hero.pos.y > Center.y + jumpDis:
            hero.jumpTo({"x": hero.pos.x - jumpDis,"y": hero.pos.y - (hero.pos.y - Center.y)})
        elif hero.pos.y < Center.y - jumpDis:
            hero.jumpTo({"x": hero.pos.x - jumpDis,"y": hero.pos.y + (Center.y - hero.pos.y)})
        else:
            hero.jumpTo({"x": hero.pos.x + jumpDis,"y": hero.pos.y})
    jumpIndex += 1
