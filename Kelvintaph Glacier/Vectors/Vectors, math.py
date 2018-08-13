# Стукай по мячу так, чтобы перебить всех синих скелетов, не трогая красных.
# Синие скелеты могут быть найдены как враги.
bro = hero.findFriends()[0]
ball = hero.findByType("ball")[0]
center = {"x": 40, "y": 35}
enemies = hero.findEnemies()

def aiming():
    skeletons = hero.findByType("skeleton", enemies)
    MAX = 0
    for enemy in skeletons:
        distance = bro.distanceTo(enemy)
        if distance > MAX and enemy.health == 300:
            MAX = distance
            targ = enemy
    if targ:
        vector = Vector.normalize(Vector.subtract(targ.pos, ball.pos))
        angle = Vector.heading(vector)
        return angle

def toPosition(angle):
    vector = Vector.subtract(bro.pos, center)
    broAngle = Vector.heading(vector)
    radius = 6
    if angle > broAngle:
        angle = angle - Math.PI
    else:
        angle = angle + Math.PI
    if broAngle < angle:
        while broAngle < angle:
            newX = center.x + (radius * Math.cos(broAngle))
            newY = center.y + (radius * Math.sin(broAngle))
            broAngle += 0.05
            hero.command(bro, "move", {"x": newX , "y": newY})
            hero.wait(0.067)
    elif broAngle > angle:
        while broAngle > angle:
            newX = center.x + (radius * Math.cos(broAngle))
            newY = center.y + (radius * Math.sin(broAngle))
            broAngle -= 0.05
            hero.command(bro, "move", {"x": newX , "y": newY})
            hero.wait(0.067)

def hit():
    position = bro.pos
    while bro.distanceTo(center) > 2:
        hero.command(bro, "move", center)
        hero.wait(0.05)
    while bro.distanceTo(position) > 2:
        hero.command(bro, "move", position)
        hero.wait(0.05)

while True:
    if bro.distanceTo(center) < 6:
        run = Vector.normalize(Vector.subtract(bro.pos, center))
        run = Vector.add(bro.pos, run)
        hero.command(bro, "move", run)
    elif ball.distanceTo(center) < 1:
        angle = aiming()
        toPosition(angle)
        hit()

#  ----------------------------------------------------------


center = Vector(40, 35)
punch_array = []
enemies = hero.findEnemies()
friend = hero.findFriends()[0]
ball = self.findNearest(self.findByType('ball'))
ballPoss = Vector(ball.pos.x, ball.pos.y)
for enemy in enemies:
    s2b = Vector.multiply(Vector.normalize(Vector.subtract(ballPoss, enemy.pos)), 7)
    b2p = ball.pos.add(s2b)
    punch_array.append(b2p)

distance = 100
while len(punch_array) > 0:
    min_dist, min_index = 999, -1
    for index, punch in enumerate(punch_array):
        if min_dist > Vector.subtract(punch, friend.pos).magnitude():
            min_dist = Vector.subtract(punch, friend.pos).magnitude()
            min_index = index
    vector = punch_array.pop(min_index)
    hero.command(friend, 'move', vector)
    hero.wait(1)
    hero.command(friend, 'move', center)
    hero.wait(1)
    hero.command(friend, 'move', vector)
