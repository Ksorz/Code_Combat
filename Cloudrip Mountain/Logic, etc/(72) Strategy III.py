# Your goal is to protect the peasant and move to the right.
# Arryn Stonewall will defend the front, and command the soldiers.
# You need to cover the rear and command the peasant.

arryn = hero.findByType("raider")[0]
peasant = hero.findByType("peasant")[0]

def chooseHeroStrategy():
    # Return either "fight" or "advance".
    # Try to stay 5m behind the peasant when not fighting.
    # Don't get more than 15m away from the peasant.
    enemies = hero.findEnemies()
    enemy = hero.findNearest(enemies)
    if enemy and hero.distanceTo(enemy) <= 45 and hero.distanceTo(peasant) <= 15 and hero.pos.x < peasant.pos.x:
        return "fight"
    else:
        return "advance"
    pass

def heroFight():
    # Stop the ogres from rushing past you to get to the peasant!
    # Hint: try to slow them down if you can
    enemy = hero.findNearestEnemy()
    if hero.canCast("slow", enemy):
        hero.cast("slow", enemy)
    else:
        hero.attack(enemy)
    pass

def heroAdvance():
    # Stay behind the peasant
    hero.moveXY(peasant.pos.x - 5, peasant.pos.y)
    pass

def choosePeasantStrategy():
    # Return "follow", "build-above", or "build-below"
    # Hint: use isPathClear() to determine where the hallways are
    above = {"x": peasant.pos.x, "y": peasant.pos.y + 10}
    below = {"x": peasant.pos.x, "y": peasant.pos.y - 10}
    if hero.isPathClear(peasant.pos, above):
        return "build-above"
    elif hero.isPathClear(peasant.pos, below):
        return "build-below"
    else:
        return "follow"
    pass

def peasantAdvance():
    # Keep the peasant behind Arryn and her soldiers.
    pos = {"x": arryn.pos.x - 5, "y": arryn.pos.y}
    hero.command(peasant, "move", pos)
    pass

def peasantBuild(x,y):
    # Command the peasant to build a palisade.
    hero.command(peasant, "buildXY", "palisade", x, y)
    pass

while True:
    heroStrategy = chooseHeroStrategy()
    if heroStrategy == "fight":
        heroFight()
    elif heroStrategy == "advance":
        heroAdvance()

    peasantStrategy = choosePeasantStrategy()
    if peasantStrategy == "build-above":
        peasantBuild(peasant.pos.x, peasant.pos.y + 5)
    elif peasantStrategy == "build-below":
        peasantBuild(peasant.pos.x, peasant.pos.y - 5)
    elif peasantStrategy == "follow":
        peasantAdvance()
