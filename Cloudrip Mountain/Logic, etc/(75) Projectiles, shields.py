# Advance through the forgotten tomb.
# Be wary, traps lay in wait to ruin your day!

# The Paladins volunteer to lead the way.
# Command them to shield against incoming projectiles.
while True:
    friends = hero.findFriends()
    # findEnemyMissiles finds all dangerous projectiles.
    projectiles = hero.findEnemyMissiles()
    for friend in friends:
        if friend.type is "paladin":
            # Find the projectile nearest to the friend:
            enemyMissiles = hero.findEnemyMissiles()
            projectile = friend.findNearest(enemyMissiles)
            # If the projectile exists
            # AND is closer than 10 meters to the paladin:
            if projectile and friend.distanceTo(projectile) < 10:
                # Command the friend to "shield":
                hero.command(friend, "shield")
            # ELSE, when there is no potential danger:
            else:
                # Advance the paladin:
                hero.command(friend, "move", {"x": friend.pos.x +1, "y": friend.pos.y})
            pass
        else:
            # If not a paladin, just advance:
            targets = hero.findByType("paladin", hero.findFriends())
            nearest = friend.findNearest(targets)
            hero.command(friend, "move", {"x": nearest.pos.x - 15, "y": nearest.pos.y})
        pass
    # Advance the hero in the x direction:
    targets = hero.findByType("paladin", hero.findFriends())
    nearest = hero.findNearest(targets)
    hero.moveXY(nearest.pos.x - 8, nearest.pos.y)
