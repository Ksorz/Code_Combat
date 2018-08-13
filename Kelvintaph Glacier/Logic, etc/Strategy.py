squad = hero.findFriends()
for friend in squad:
    if friend.type == "soldier":
        if friend.pos.y > 45:
            girl = friend
        else:
            boy = friend

girlpoint = {"x": 18, "y": 58}
girlpoint2 = {"x": 31, "y": 52}
girlpoint3 = {"x": 29, "y": 39}

safepoint = {"x": 12, "y": 44}

GI = 0
GI2 = 0
GI3 = 0

goal1 = {"x": 50, "y": 58}
goal2 = {"x": 50, "y": 38}
GOAL = {"x": 77, "y": 40}

def chooseStrategy():
    if hero.canCast("poison-cloud") and enemies.length > 5 and poisonPlace():
        hero.cast("poison-cloud", poisonPlace())
    elif enemy and hero.canCast("chain-lightning", enemy):
        return "fight"
    elif hero.canCast("raise-dead") and around(hero, hero.findCorpses(), 20) >= 4:
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
    maxCount = 4
    victim = None
    for enemy in enemies:
        count = around(enemy, enemies, 10)
        if count > maxCount:
            maxCount = count
            victim = enemy
    return victim

def summon():
    if hero.canCast("summon-burl"):
        hero.cast("summon-burl")
    elif hero.canCast("summon-undead"):
        hero.cast("summon-undead")

def lowestHP():
    target = None
    lowest = 999999
    for enemy in squadEnemies:
        if enemy.health < lowest and enemy.health > 0:
            lowest = enemy.health
            target = enemy
    return target

def inTarget(unit):
    count = 0
    for enemy in squadEnemies:
        if enemy.target == unit:
            count += 1
    if count > 1:
        return True
    else:
        return False

def command():
    for friend in squad:
        enemy = friend.findNearestEnemy()
        if squadEnemies.length > 0 and friend.type == "soldier":
            if witch:
                if friend == girl:
                    if friend.distanceTo(girlpoint) > 1 and GI == 0:
                        hero.command(friend, "move", girlpoint)
                    else:
                        hero.command(friend, "attack", witch)
                        GI += 1
                elif friend == boy:
                    hero.command(friend, "attack", enemy)
            else:
                if friend == girl:
                    if friend.distanceTo(girlpoint2) > 1  and GI2 == 0:
                        hero.command(friend, "move", girlpoint2)
                    elif friend.distanceTo(girlpoint3) > 1  and GI3 == 0:
                        hero.command(friend, "move", girlpoint3)
                        GI2 += 1
                    elif friend.distanceTo(safepoint) > 1:
                        hero.command(friend, "move", safepoint)
                        GI3 += 1
                elif friend == boy:
                    if friend.health > 30:
                        hero.command(friend, "attack", enemy)
                    else:
                        hero.command(friend, "move", safepoint)
                else:
                    hero.command(friend, "move", safepoint)
                    BI += 1
        elif squadEnemies.length > 0 and friend.type == "archer":
            hero.command(friend, "attack", lowestHP())
        elif squadEnemies.length > 0 and friend.type == "paladin":
            if friend.canCast("heal") and friend.health < 400:
                hero.command(friend, "cast", "heal", friend)
            elif inTarget(friend):
                hero.command(friend, "shield")
            else:
                hero.command(friend, "attack", enemy)
        else:
            if friend.pos.x < 49:
                hero.command(friend, "move", goal1)
            elif friend.pos.y > 40:
                hero.command(friend, "move", goal2)
            else:
                hero.command(friend, "move", GOAL)

def fight():
    if enemy:
        missile = hero.findEnemyMissiles()[0]
        if missile and hero.distanceTo(missile) < 15:
            hero.move({"x": hero.pos.x - 1, "y": hero.pos.y})
        elif hero.isReady("devour") and hero.distanceTo(enemy) < 20 and enemy.health > 135:
            hero.devour(enemy)
        elif hero.canCast("chain-lightning", enemy):
            hero.cast("chain-lightning", enemy)
        else:
            hero.attack(enemy)
    else:
        hero.move({"x": 78, "y": 14})

while True:
    enemies = hero.findEnemies()
    heroEnemies = []
    squadEnemies = []
    witch = hero.findByType("witch")[0]
    ogres = hero.findByType("ogre")
    for enemy in enemies:
        if enemy.pos.y < 31:
            heroEnemies.append(enemy)
        elif enemy.pos.y > 31:
            squadEnemies.append(enemy)
    enemy = hero.findNearest(heroEnemies)
    command()
    strategy = chooseStrategy()
    if strategy == "fight":
        fight()
    elif strategy == "summon":
        summon()
