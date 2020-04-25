from random import randint
import keyboard
import sys
import os
import time

######### global variables we'll be using all over the places #######
meSymbol = '☻'
posXme = randint(1, 11)
posYme = randint(1, 5)
loveSymbol = '♥'
posXlove = randint(1, 11)
posYlove = randint(1, 5)
mapwidth = 14
mapheight = 5

################

def buildMap(w, h): # creates the map
    builtMap = " "
    for _ in range(w-2):
        builtMap += '-'
    for _ in range(h):
        builtMap += '\n'
        builtMap += '|'
        for _ in range(w-2):
            builtMap += ' '
        builtMap += '|'
    builtMap += '\n '
    for _ in range(w-2):
        builtMap += '-'
    return builtMap

MAP = buildMap(mapwidth, mapheight)
# # debug or print to see it, but by default this made a map like this:
# MAP = """ ------------ 
# |            |
# |            |
# |            |
# |            |
# |            |
#  ------------
# """


######### I define some functions we'll be calling often during our game #######
# draws whatever you pass it into the preset map (which is really one big string)
def drawThingAt(drawme, y, x, currentmap):
    mypos = mapwidth*y + x  # convert y and x into a single counter from beginning of string
    # string can't be altered, so we convert our string to a list
    newmap = list(currentmap)
    newmap[mypos] = drawme  # and then we insert our thing into that list
    # force cast the list back into a string and return it to be (possibly) altered further later
    return "".join(newmap)


def delay_print(s, sleeptime=0.05):  # prints char to screen w super cool delay, will need explicit new line to get one
    for c in s:  # go through all of the characters in the string
        # write single char to screen, which normally wouldn't print until newline
        sys.stdout.write(c)
        sys.stdout.flush()  # forces single char to screen, doesn't wait for newline
        time.sleep(sleeptime)  # artistic pause, optional parameter to function


############################################################################
############################################################################
# !!! all of your modifications will be below this line ###
# TODO 1) make your character walk around the screen
# TODO 2) make your character unable to travel thru walls #
# TODO 3) draw the elusive love to the screen 
# TODO 4) when your character enters the same square as elusive_love, you have won the game. indicate this somehow to the player.
# TODO 5) do as much as you want to expand the game and make it more fun for you! the more you do the more you'll learn

######### start our program here #######
os.system('cls' if os.name == 'nt' else 'clear')  # clears screen
delay_print("RikiT♣ki G♠mes presents:\n")
delay_print("Test 3 -- THE GAME")
time.sleep(1)
while True:
    os.system('cls' if os.name == 'nt' else 'clear')  # clears screen
    currentmap = drawThingAt(meSymbol, posYme, posXme, MAP)
    print(currentmap)
    time.sleep(0.1)
    key = keyboard.read_key()
    if key == 'w':
        pass
    if key == 'a':
        pass
    if key == 's':
        pass
    if key == 'd':
        pass
    if key == 'q':
        delay_print("you have quit. bye bye now\n")
        sys.exit(0)
