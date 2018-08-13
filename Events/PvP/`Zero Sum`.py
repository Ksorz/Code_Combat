allTypes = "soldier" or "archer" or "griffin-rider" or "artillery" or "paladin" or "sorcerer"

soldier = "soldier"
archer = "archer"
griffin_rider = "griffin-rider"
artillery = "artillery"
paladin = "paladin"
sorcerer = "sorcerer"
cage = "cage"
yeti = "yeti"

king = hero.findByType("sorcerer")[0]


def num_DisLimit(target, DisLimit):
    Index = 0
    num = 0
    while len(target) > Index:
        obj = target[Index]
        if hero.distanceTo(obj) <= DisLimit:
            num += 1
        Index += 1
    return num

def bestCoin(coins):
    Index = 0
    Maxrating = 0
    bestCoin = None
    while len(coins) > Index:
        coin = coins[Index]
        coinrating = coin.value / hero.distanceTo(coin)
        if coinrating > Maxrating:
            Maxrating = coinrating
            bestCoin = coin
        Index += 1
    return bestCoin

def dis_SumCoins(coins, dis):
    Index = 0
    SumCoins = 0
    while len(coins) > Index:
        coin = coins[Index]
        distance = hero.distanceTo(coin)
        if distance <= dis:
            SumCoins += coin.value
        Index += 1
    return SumCoins

def lowestHP(targets, Type):
    lowest = None
    lowestHP = 99999
    Index = 0
    while len(targets) > Index:
        tar = targets[Index]
        targetHP = tar.health
        if tar.type != cage and tar.type != yeti:
            if tar.type == Type and lowestHP > targetHP and lowestHP > 0:
                targetHP = lowestHP
                lowest = tar
        Index += 1
    if lowest != None:
        return lowest
    else:
        return king

def Type(targets, Type):
    obj = None
    Index = 0
    while len(targets) > Index:
        target = targets[Index]
        if target.type == Type:
            obj += target
        Index += 1
    return obj

def who_to_summon():
    friends = hero.findFriends()
    enemies = hero.findEnemies()
    Fsold_num = hero.findByType("soldier", friends)
    Farch_num = hero.findByType("archer", friends)
    Fgrif_num = hero.findByType("griffin-rider", friends)
    Esold_num = hero.findByType("soldier", enemies)
    Earch_num = hero.findByType("archer", enemies)
    Egrif_num = hero.findByType("griffin-rider", enemies)
    if len(enemies) >= 8 and len(friends) <= 2:
        if hero.gold >= hero.costOf("artillery"):
            hero.summon("artillery")
    elif len(Fsold_num) < 2:
        if hero.gold >= hero.costOf("soldier"):
            hero.summon("soldier")
    elif len(Earch_num) >= 3 or len(Fgrif_num) < 2:
        if hero.gold >= hero.costOf("griffin-rider"):
            hero.summon("griffin-rider")
    elif len(Farch_num) < 1:
        if hero.gold >= hero.costOf("archer"):
            hero.summon("archer")
    elif hero.gold >= hero.costOf("paladin"):
        hero.summon("paladin")



def gather_run_tactics():
    while dis_SumCoins(hero.findItems(), 20) > 10:
        coin = bestCoin(hero.findItems())
        if hero.isPathClear(self.pos, coin.pos):
            hero.move(coin.pos)
        else:
            hero.moveXY(39, 29)

        hero_behaviour()
        who_to_summon()
        ally_attack_tactic()

def ally_attack_tactic():
    friends = hero.findFriends()
    enemies = hero.findEnemies()
    lowestUnit = lowestHP(enemies, allTypes)
    Fsold_num = hero.findByType("soldier", friends)
    Farch_num = hero.findByType("archer", friends)
    Fgrif_num = hero.findByType("griffin-rider", friends)
    Esold_num = hero.findByType("soldier", enemies)
    Earch_num = hero.findByType("archer", enemies)
    Egrif_num = hero.findByType("griffin-rider", enemies)
    for griffin_rider in friends:
        if len(Fsold_num) > 0 and Fsold_num[0].distanceTo(lowestUnit) > 15:
            hero.command(griffin_rider, "move", target)
        if len(Earch_num) > 0:
            hero.command(griffin_rider, "attack", lowestHP(enemies, "archer"))
        elif len(Egrif_num) > 0:
            hero.command(griffin_rider, "attack", lowestHP(enemies, "griffin-rider"))











def hero_behaviour():
    enemies = hero.findEnemies()
    if len(enemies) >= 5 and hero.isReady("mana-blast"):
        hero.jumpTo({"x": lowestHP(enemies, allTypes).pos.x, "y": lowestHP(enemies, allTypes).pos.y})
        hero.say("AAAAAAAAAAAAAAAAA")
        hero.manaBlast()
    if hero.canCast("goldstorm"):
        hero.cast("goldstorm")
    if hero.canCast("fear") and hero.distanceTo(king) < 28:
        hero.cast("fear", king)





while True:
    gather_run_tactics()

        # while break

    hero_behaviour()

    hero.attack(lowestHP(hero.findEnemies(), allTypes))

    ally_attack_tactic()
