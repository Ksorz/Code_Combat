# Хашбаум попала в засаду огров!
# Она занята исцелением своих солдат, так что прикажи им сражаться!
# Огры вызовут подкрепление, если посчитают, что смогут добраться до Хашбаум или лучников. Поэтому выстрой их в оборонительное кольцо!

# Солдаты формируют круг и защищаются.
def commandSoldier(soldier, soldierIndex, numSoldiers):
    angle = Math.PI * 2 * soldierIndex / numSoldiers
    defendPos = {"x": 41, "y": 40}
    defendPos.x += 10 * Math.cos(angle)
    defendPos.y += 10 * Math.sin(angle)
    hero.command(soldier, "defend", defendPos);

# Найди самого сильного врага (с наибольшим здоровьем)
# Эта функция что-то возвращает! Когда ты её вызываешь, то получаешь назад некоторое значение.
def findStrongestTarget():
    mostHealth = 0
    bestTarget = None
    enemies = hero.findEnemies()
    # Определи, у кого из врагов наибольший уровень здоровья, и присвой это значение переменной `bestTarget`.
    for enemy in enemies:
        if mostHealth < enemy.health:
            bestTarget = enemy
            mostHealth = enemy.health
    # Концентрируй огонь лучников на одном противнике, когда нападает большой огр.
    if bestTarget and bestTarget.health > 15:
        return bestTarget
    else:
        return None


# Если у врага `strongestTarget` больше 15 единиц здоровья, атакуй его. Иначе атакуй ближайшего врага.
def commandArcher(archer):
    nearest = archer.findNearestEnemy()
    if archerTarget:
        hero.command(archer, "attack", archerTarget)
    elif nearest:
        hero.command(archer, "attack", nearest)

archerTarget = None

while True:
    # Если враг `archerTarget` повержен или не существует, найди нового.
    if not archerTarget or archerTarget.health <= 0:
        # Установи в переменную `archerTarget` результат, который возвращает функция `findStrongestTarget()`
        archerTarget = findStrongestTarget()

    friends = hero.findFriends()
    soldiers = hero.findByType("soldier")
    # Создай переменную, указывающую на твоих лучников.
    archers = hero.findByType("archer")
    for i in range(len(soldiers)):
        soldier = soldiers[i]
        commandSoldier(soldier, i, len(soldiers));
    # используй функцию `commandArcher()` для управления своими лучниками
    for i in range(len(archers)):
        archer = archers[i]
        commandArcher(archer)
