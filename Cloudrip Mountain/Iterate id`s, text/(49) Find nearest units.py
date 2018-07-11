# You need to distract "Big Bertha" until you special squad arrives.
# The cannon shoots at the pair of soldiers closest to each other.

# This function finds the pair of units
# with the minimum distance between them.
def findNearestPair(units):
    minDistance = 9001
    nearestPair = ["Nobody", "Nobody"]
    # You need to check and compare all pairs of units.
    # Iterate all units with indexes "i" from 0 to "len(units)".
    for i in range(len(units)):
        # Iterate all units again with indexes "j".
        for j in range(len(units)):
            # If "i" is equal to "j", then skip (continue).
            if i == j:
                continue
            # Find the distance between the i-th and j-th units.
            dist = units[i].distanceTo(units[j])
            # If the distance less than 'minDistance':
            if dist < minDistance:
                # Reassign 'minDistance' with the new distance.
                minDistance = dist
                # Reassign 'nearestPair' to the names
                # of the current pair of units.
                nearestPair = [units[i].id, units[j].id]
    return nearestPair


while True:
    soldiers = hero.findByType("soldier")
    # We know when the cannon shoots.
    if hero.time % 8 == 5:
        # Find which pair of soldiers in danger and protect them.
        pairOfNames = findNearestPair(soldiers)
        # Say the soldier's names and wizards will protect them.
        hero.say(pairOfNames[0] + " " + pairOfNames[1])
