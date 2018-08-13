def forDevour(enemies):
    devourHim = None
    distArr = []
    for enemy in enemies:
        if hero.distanceTo(enemy) < 6:
            distArr.append(enemy)
    max = 0
    if distArr.length > 0:
        for enemy in distArr:
            if enemy.health <= 200 and enemy.health > max:
                max = enemy.health
                devourHim = enemy
    return devourHim

def deadAround(corpses):
    dead = []
    for corpse in corpses:
        if hero.distanceTo(corpse) <= 20:
            dead.append(corpse)
    return dead.length

while True:
    enemies = hero.findEnemies()
    enemy = hero.findNearest(enemies)
    flag = hero.findFlag()
    devourHim = forDevour(enemies)
    corpses = hero.findCorpses()
    if flag:
        hero.move(flag.pos)
    if devourHim and hero.isReady("devour"):
        hero.devour(devourHim)
    elif hero.canCast("summon-burl"):
        hero.cast("summon-burl")
    elif hero.canCast("summon-undead"):
        hero.cast("summon-undead")
    elif hero.canCast("raise-dead") and deadAround(corpses) >= 3:
        hero.cast("raise-dead")
    elif enemy and hero.canCast("chain-lightning", enemy):
        hero.cast("chain-lightning", enemy)
    elif enemy and hero.canCast("poison-cloud", enemy):
        hero.cast("poison-cloud", enemy)
    elif enemy and hero.health < 1600 and hero.canCast("drain-life", enemy):
        hero.cast("drain-life", enemy)
    elif enemy:
        hero.attack(enemy)
