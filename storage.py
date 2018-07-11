# Ogres mined the field to protect their Chieftain.
# But we can use the "domino" effect get our target.
# The scout has prepared the map of the minefield.
# All mines are placed the same distance apart.
# The map is an array of strings, where "x" is a mine and "." is nothing.
# The first row in the array is the row nearest to the hero.

# The map and helpful constants are listed below.
fieldMap = hero.findFriends()[0].getMap()

mine = "x"
empty = "."
mineDistance = 5
firstXPos = 15
firstYPos = 40

# Find which starting mine connects to the ogre Chieftain.
for j in range(len(fieldMap[0])):
    winIndex = 0
    ii = 0
    jj = j
    done = []
    if fieldMap[ii][jj] == empty:
        continue
    while winIndex < len(fieldMap) - 1:
        isUp = fieldMap[ii+1][jj]
        isRt = fieldMap[ii][jj+1]
        IsLt = fieldMap[ii][jj-1]
        isDn = fieldMap[ii-1][jj]
        if isUp == mine and [ii+1, jj] not in done:
            winIndex += 1
            ii += 1
        elif isRt == mine and [ii, jj+1] not in done:
            jj += 1
        elif IsLt == mine and [ii, jj-1] not in done:
            jj -= 1
        elif isDn == mine and [ii-1, jj] not in done:
            winIndex -= 1
            ii -= 1
        else:
            break
        done.append([ii, jj])
    if winIndex == len(fieldMap) - 1:
        resultColumn = j
        break













# Find which starting mine connects to the ogre Chieftain.
for j in range(len(fieldMap[0])):
    for i in range(len(fieldMap)):
        winIndex = 0
        ii = i
        jj = 0
        done = []

        hero.say(j + " " + i)
        while winIndex < len(fieldMap) - 1:
            isUp = fieldMap[ii+1][jj]
            isRt = fieldMap[ii][jj+1]
            IsLt = fieldMap[ii][jj-1]
            isDn = fieldMap[ii-1][jj]
            ij = [ii, jj]
            if isUp == mine and ij not in done:
                winIndex += 1
                ii += 1
                done.append(ij)
            elif isRt == mine and ij not in done:
                jj += 1
                done.append(ij)
            elif IsLt == mine and ij not in done:
                jj -= 1
                done.append(ij)
            elif isDn == mine and ij not in done:
                winIndex -= 1
                ii -= 1
                done.append(ij)
            else:
                break
        if winIndex == len(fieldMap) - 1:
            startingMine = j
            hero.say(j)
            break
    if winIndex == len(fieldMap) - 1:
        break




# Find which starting mine connects to the ogre Chieftain.
for j in range(len(fieldMap[0])):
    hero.say("lol")
    winIndex = 0
    ii = 0
    jj = j + 12
    done = []
    if fieldMap[ii][jj] == empty:
        continue
    while winIndex < 15:
        isUp = fieldMap[ii+1][jj]
        isRt = fieldMap[ii][jj+1]
        IsLt = fieldMap[ii][jj-1]
        isDn = fieldMap[ii-1][jj]
        hero.say(ii + " : " + jj + " (" + winIndex + ")" + " " + len(done))
        ij = [ii, jj]
        done.append(ij)
        if isUp == mine and not done.count([ii + 1, jj]):
            winIndex += 1
            ii += 1
            hero.say(done[-1][0] + " " + done[-1][1])
        elif isRt == mine:
            if done.count([ii, jj + 1]):
                hero.say("message")
            else:
                jj += 1
                hero.say(done[-1][0] + " " + done[-1][1])
        elif IsLt == mine and not done.count([ii, jj - 1]):
            jj -= 1
            hero.say(done[-1][0] + " " + done[-1][1])
        elif isDn == mine and not done.count([ii - 1, jj]):
            winIndex -= 1
            ii -= 1
            hero.say(done[-1][0] + " " + done[-1][1])
        else:
            break
    if winIndex == 15:
        startingMine = j
        hero.say(j)
        break




done.append(ii + ":" + jj)
        hero.say(ii + ":" + jj + " (" + winIndex + ")" + " " + len(done))
        if len(done) > 4:
            hero.say(done[-1] + " " + done[-2] + " " + done[-3] + " " + done[-4])
        if isExist(done, ii + ":" + jj-1):
            hero.say("Exist")
        else:
            hero.say("Not Exist")



hero.say(Y + " : " + X + " (" + winIndex + ")" + " " + len(done) + " : " + len(banned))
hero.say(done[-1][0] + " " + done[-1][1])
hero.say(winIndex + ' ' + j)
hero.say(Y + " : " + X + " (" + winIndex + ")" + fieldMap[Y][jj-1] + " " + fieldMap[Y][X+1])



def isExist(arr, ele):
    for i in arr:
        if i == ele:
            return True
    return False



array = []
array.push([1, 7])
array









def switch(Y, X):
    isUp = fieldMap[Y+1][X]
    isRt = fieldMap[Y][X+1]
    IsLt = fieldMap[Y][X-1]
    isDn = fieldMap[Y-1][X]
    while turnIndex % 4 == 0: # UP (RT)
        if isRt == mine:
            turnIndex += 1
        else:
            if isUp == mine:
                Y += 1
    while turnIndex % 4 == 1: # RT (DN)
        if isDn == mine:
            turnIndex += 1
        else:
            if isRt
    while turnIndex % 4 == 2: # DN (LT)

    while turnIndex % 4 == 3: # LT (UP)




def alwaysRightsolution(Y, X):
    turnIndex = 0
    direction = fieldMap[switch(Y, X)]
















# Find which starting mine connects to the ogre Chieftain.
for j in range(len(fieldMap[0])):
    winIndex = 0
    Y = 0
    X = j
    done = [[None][None]]
    if fieldMap[Y][X] == empty:
        continue
    else:
        start = fieldMap[Y][X]
        alwaysRightsolution(fieldMap[Y][X])
