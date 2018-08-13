startPos = {"x": 61, "y": 64}
friendPos = Vector(61, 54)

# Settings
rangeUnits = ["shaman", "thrower", "fangrider", "headhunter", "archer"]
commTypes = ["skeleton", "soldier", "archer", "griffin-rider", "paladin", "peasant"]
# --------

def chooseStrategy():
    if hero.health < 600 and hero.findNearest(friends) and hero.distanceTo(hero.findNearest(friends)) < 30 and hero.canCast("sacrifice", sacrifice(friends), hero):
        hero.cast("sacrifice", sacrifice(friends), self)
    elif hero.canCast("poison-cloud") and enemies.length > 30 and poisonPlace():
        hero.cast("poison-cloud", poisonPlace())
    elif hero.canCast("raise-dead") and len(around(hero, hero.findCorpses(), 20)) >= 7:
        hero.cast("raise-dead")
    elif hero.canCast("summon-burl") or hero.canCast("summon-undead"):
        return "summon"
    elif enemy and hero.canCast("chain-lightning", enemy):
        return "fight"
    else:
        return "fight"

def sacrifice(friends):
    hp = 0
    victim = None
    for friend in friends:
        if friend.health > hp and hero.distanceTo(friend) < 30:
            hp = friend.health
            victim = friend
    return victim

def excludedTarget(units, targ):
    array = []
    for unit in units:
        if unit.target != targ.id:
            array.append(unit)
    return array

def around(unit, units, dis):
    count = []
    for i in range(len(units)):
        distance = unit.distanceTo(units[i])
        if distance <= dis:
            count.append(units[i])
    return count

def poisonPlace():
    distance = hero.distanceTo(hero.findNearestEnemy())
    for enemy in enemies:
        check = hero.distanceTo(enemy)
        if check > distance + 8 and check < distance + 20:
            victim = enemy
            break
    return victim

def targetAoe(units, unitType, aoe):
    target = None
    for unit in units:
        if unit.type in unitType:
            target = unit
            break
    if not target:
        target = hero.findNearestEnemy()
    return target

def forDevour(enemies):
    victim = None
    MIN = 130
    for enemy in enemies:
        dist = hero.distanceTo(enemy)
        if dist < 11 and enemy.health > MIN and enemy.health <= 200:
            MIN = enemy.health
            victim = enemy
            if MIN > 190:
                break
    return victim

def minionTarget(enemies, enemyType, friend, rad):
    closest = None
    closestDis = 9999
    for enemy in enemies:
        distance = friend.distanceTo(enemy)
        if distance <= rad and distance < closestDis:
            closest = enemy
            closestDis = distance
    if not closest:
        closest = friend.findNearestEnemy()
    return closest

def summon():
    if hero.gold >= hero.costOf("soldier"):
        hero.summon("soldier")
    elif hero.canCast("summon-burl"):
        hero.cast("summon-burl")
        hero.wait(0.05)
    elif hero.canCast("summon-undead"):
        hero.cast("summon-undead")
        hero.wait(0.05)

def command():
    near = {"x": hero.pos.x - 3, "y": hero.pos.y}
    for friend in friends:
        if friend.type in commTypes:
            target = minionTarget(enemies, rangeUnits, friend, 8)
            if target:
                hero.command(friend, "attack", target)
            elif friend.distanceTo(friendPos) > 10:
                hero.command(friend, "move", friendPos)

def fight():
    if hero.health < 1200 and len(around(hero, enemies, 15)) > 4 and hero.distanceTo(startPos) > 4:
        hero.moveXY(startPos.x, startPos.y)
    target = targetAoe(enemies, rangeUnits, 5)
    if target:
        devour = forDevour(enemies)
        distance = hero.distanceTo(target)
        if devour and hero.isReady("devour"):
            hero.devour(devour)
        elif hero.canCast("chain-lightning", target) and distance <= 25:
            hero.cast("chain-lightning", target)
        elif hero.health < 1600 and hero.canCast("drain-life", target) and distance <= 15:
            hero.cast("drain-life", target)
        elif target and distance <= 70:
            hero.attack(target)
        else:
            hero.move(startPos)
    if hero.distanceTo(startPos) > 6 and hero.isReady("jump"):
        hero.jumpTo(startPos)

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
