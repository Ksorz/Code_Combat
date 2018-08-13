enemies = hero.findEnemies()
hp = 0
for enemy in enemies:
    if enemy.health > hp:
        hp = enemy.health
        CRAB = enemy
if hero.pos.x > 80:
    startPos = {"x": 120, "y": 41}

else:
    startPos = {"x": 40, "y": 94}
# Settings
dungerLevel = CRAB.health / 200
Center = {"x": 80, "y": 69}
rangeUnits = ["shaman", "thrower", "fangrider", "headhunter", "archer"]
commTypes = ["skeleton", "soldier", "archer", "griffin-rider", "paladin", "peasant"]
# --------

def chooseStrategy():
    if hero.health < 600 and hero.findNearest(friends) and hero.distanceTo(hero.findNearest(friends)) < 30 and hero.canCast("sacrifice", sacrifice(friends), hero):
        hero.cast("sacrifice", sacrifice(friends), self)
    elif hero.canCast("poison-cloud") and enemies.length > 15 and poisonPlace():
        hero.cast("poison-cloud", poisonPlace())
        hero.wait(0.05)
    elif hero.canCast("raise-dead") and len(around(hero, hero.findCorpses(), 20)) >= 5:
        hero.cast("raise-dead")
        hero.wait(0.05)
    elif hero.canCast("summon-burl") or hero.canCast("summon-undead"):
        return "summon"
    elif hero.distanceTo(CRAB) < dungerLevel:
        if hero.canCast("fear"):
            return "fight"
        RUN = whereToRun(hero, CRAB, dungerLevel * 1.2, 11)
        hero.move(RUN)
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

def whereToRun(runner, dunger, radius, step):
    if hero.pos.x > 70 and hero.pos.x < 90 and hero.pos.y > 60 and hero.pos.y < 80:
        return startPos
    runHere = None
    aX = runner.pos.x - dunger.pos.x
    aY = runner.pos.y - dunger.pos.y
    angle = Math.atan2(aY, aX)
    step = step / radius
    while True:
        angle -= step
        newX = dunger.pos.x + (radius * Math.cos(angle))
        newY = dunger.pos.y + (radius * Math.sin(angle))
        runHere = Vector(newX, newY)
        if hero.isPathClear(hero.pos, runHere):
            break
        else:
            while True:
                angle += step
                newX = dunger.pos.x + (radius * Math.cos(angle))
                newY = dunger.pos.y + (radius * Math.sin(angle))
                runHere = Vector(newX, newY)
                if hero.isPathClear(hero.pos, runHere):
                    break
        break
    return runHere

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
    maxCount = 5
    victim = None
    for enemy in enemies:
        if hero.distanceTo(enemy) < 40:
            countEne = around(enemy, excludedTarget(enemies, CRAB), 10)
            count = len(countEne)
            if CRAB in countEne or enemy == CRAB:
                count += 10
            if count > maxCount:
                maxCount = count
                victim = enemy
    return victim

def targetAoe(enemies, enemyType, aoe):
    correctType = []
    target = None
    for unit in enemies:
        if unit.type in enemyType:
            correctType.append(unit)
    correctType = excludedTarget(correctType, CRAB)
    if correctType.length > 2:
        maximum = 1
        for unit in correctType:
            count = len(around(unit, correctType, aoe))
            if maximum < count and hero.distanceTo(unit) <= 40 and hero.isPathClear(hero.pos, unit.pos):
                maximum = count
                target = unit
    if not target:
        target = hero.findNearestEnemy()
    return target

def forDevour(enemies):
    victim = None
    MIN = 130
    for enemy in enemies:
        dist = hero.distanceTo(enemy)
        if dist < 11 and enemy.health > MIN and enemy.health <= 200:
            min = enemy.health
            victim = enemy
    return victim

def minionTarget(enemies, friend):
    cleared = excludedTarget(enemies, CRAB)
    enemy = friend.findNearest(cleared)
    if enemy and friend.distanceTo(enemy) < 35:
        return enemy

def summon():
    if hero.gold >= hero.costOf("griffin-rider"):
        hero.summon("griffin-rider")
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
            target = minionTarget(enemies, friend)
            if len(around(hero, enemies, 20)) > 5:
                hero.command(friend, "defend", hero)
            elif hero.health < 1300:
                hero.command(friend, "defend", hero)
            elif friend.type == "skeleton":
                if target and friend.distanceTo(hero) < 25:
                    hero.command(friend, "attack", target)
                elif target:
                    hero.command(friend, "defend", hero)
            elif friend.type == "griffin-rider":
                if target and friend.distanceTo(hero) < 15:
                    hero.command(friend, "attack", target)
                elif target:
                    hero.command(friend, "defend", hero)

def fight():
    if hero.health < 1200 and len(around(hero, enemies, 15)) > 4 and hero.distanceTo(startPos) > 4:
        hero.moveXY(startPos.x, startPos.y)
    target = targetAoe(enemies, rangeUnits, 4)
    if target:
        devour = forDevour(enemies)
        distance = hero.distanceTo(target)
        if hero.canCast("fear", CRAB) and hero.distanceTo(CRAB) <= 25:
            hero.cast("fear", CRAB)
            hero.wait(0.05)
        elif devour and hero.isReady("devour"):
            hero.devour(devour)
            hero.wait(0.05)
        elif hero.canCast("chain-lightning", target) and distance <= 25:
            hero.cast("chain-lightning", target)
            hero.wait(0.05)
        elif hero.health < 1600 and hero.canCast("drain-life", target) and distance <= 15:
            hero.cast("drain-life", target)
        elif target and distance <= 45:
            hero.attack(target)
        else:
            hero.move(startPos)
    if hero.distanceTo(CRAB) > 70 and hero.distanceTo(startPos) > 6:
        if hero.isReady("jump"):
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
