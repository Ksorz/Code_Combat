# The goal is to survive for 30 seconds, and keep the mines intact for at least 30 seconds.

def chooseStrategy():
    if hero.canCast("haste"):
        hero.cast("haste", self)
    enemy = hero.findNearestEnemy()
    # If you can summon a griffin-rider, return "griffin-rider"
    if hero.gold >= hero.costOf("griffin-rider"):
        return "griffin-rider"
    # If there is a fangrider on your side of the mines, return "fight-back"
    elif enemy and enemy.pos.x < 36:
        return "fight-back"
    # Otherwise, return "collect-coins"
    else:
        return "collect-coins"

def commandAttack():
    # Command your griffin riders to attack ogres.
    for friend in hero.findFriends():
        enemy = friend.findNearestEnemy()
        if enemy and friend.health < friend.maxHealth * 0.8 and friend.distanceTo(enemy) < 7:
            hero.command(friend, "move", {'x': friend.pos.x - 7, 'y': friend.pos.y})
        elif enemy:
            hero.command(friend, "attack", enemy)
    pass
def bestCoin(coins):
    bestValue = 0
    for i in coins:
        bestI = i.value / hero.distanceTo(i)
        if bestI > bestValue:
            bestValue = bestI
            best = i
    return best
def pickUpCoin():
    # Collect coins
    coin = bestCoin(hero.findItems())
    hero.move(coin.pos)
    pass
def heroAttack():
    # Your hero should attack fang riders that cross the minefield.
    enemy = hero.findNearestEnemy()
    hero.attack(enemy)
    pass
while True:
    commandAttack()
    strategy = chooseStrategy()
    # Call a function, depending on what the current strategy is.
    if strategy == "griffin-rider":
        hero.summon("griffin-rider")
    if strategy == "fight-back":
        commandAttack()
        heroAttack()
    if strategy == "collect-coins":
        commandAttack()
        pickUpCoin()
