# There are four pairs of twins, they should pray by pairs.
# You need to find twins and call them.

# Twins have the same names, only the last letter is different.
# This function checks if the pair of units are twins.
def areTwins(unit1, unit2):
    name1 = unit1.id
    name2 = unit2.id
    if name1.length != name2.length:
        return False
    for i in range(name1.length - 1):
        if name1[i] != name2[i]:
            return False
    return True

# Iterate over all pairs of paladins and
#  say() their name by pairs if they are twins.
friends = hero.findFriends()
for i in range(len(friends)):
    for j in range(len(friends)):
        if i >= j:
            continue
        if areTwins(friends[i], friends[j]):
            # For example: hero.say("NameTwin1 NameTwin2")
            hero.say(friends[i] + ' ' + friends[j])
# When twins are in their spots, lure the ogre.
# Don't be afraid of beams - they are dangerous only for ogres.
hero.moveXY(64, 37)
hero.moveXY(14, 37)
