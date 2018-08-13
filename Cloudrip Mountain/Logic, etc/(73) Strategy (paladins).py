# Your goal is to protect Reynaldo

# Find the paladin with the lowest health.
def lowestHealthPaladin():
    lowestHealth = 99999
    lowestFriend = None
    friends = hero.findFriends()
    for friend in friends:
        if friend.type != "paladin":
            continue
        if friend.health < lowestHealth and friend.health < friend.maxHealth / 1.4 and not friend.hasEffect("heal"):
            lowestHealth = friend.health
            lowestFriend = friend
    return lowestFriend

def commandPaladin(paladin):
    # Heal the paladin with the lowest health using lowestHealthPaladin()
    # You can use paladin.canCast("heal") and command(paladin, "cast", "heal", target)
    # Paladins can also shield: command(paladin, "shield")
    # And don't forget, they can attack, too!
    poor = lowestHealthPaladin()
    if poor and paladin.canCast("heal"):
        hero.command(paladin, "cast", "heal", poor)
    elif paladin.health < paladin.maxHealth / 3:
        hero.command(paladin, "shield")
    else:
        enemy = paladin.findNearestEnemy()
        hero.command(paladin, "attack", enemy)
    pass

def bestCoinGather(friend, claimed):
    items = hero.findItems()
    rating = 0
    for item in items:
        if item in claimed:
            continue
        else:
            value = item.value / friend.distanceTo(item)
            if rating < value:
                rating = value
                best = item
    return best


def commandFriends():
    # Command your friends.
    claimeditems = []
    friends = hero.findFriends()
    for friend in friends:
        if friend.type == "peasant":
            item = bestCoinGather(friend, claimeditems)
            claimeditems.append(item)
            hero.command(friend, "move", item.pos)
            pass
        elif friend.type == "griffin-rider":
            enemy = friend.findNearestEnemy()
            hero.command(friend, "attack", enemy)
            pass
        elif friend.type == "paladin":
            commandPaladin(friend)
            pass


while True:
    commandFriends()
    # Summon griffin riders!
    if hero.gold >= hero.costOf("griffin-rider"):
        hero.summon("griffin-rider")
