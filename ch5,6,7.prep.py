import keyboard
import time

x = 5
while x > 0 and x < 10:
    print()
    print(x)
    print("'W' to go up, 'S' to go down")
    time.sleep(0.1) # slight pause so we don't get a million key presses on accident
    key = keyboard.read_key() # read keyboard input
    if key == 'w':
        x += 1
    if key == 's':
        x -= 1
print("X reached {}!".format(x))

def changeCharAt(string, char, pos): #changes string string to have char char at position pos
    newstring = list(string) # strings are immutable (cant be directly changed), so i make it into a list
    newstring[pos] = char 
    return "".join(newstring) # weird but effective way to force cast list back to string

print()
string = "......"
print(string)
string = changeCharAt(string, 'd', 3)
print(string)
string = changeCharAt(string, 'f', 5)
print(string)
string = changeCharAt(string, 'a', 0)
print(string)
string = changeCharAt(string, '.', 3)
print(string)
string = changeCharAt(string, '.', 5)
print(string)
string = changeCharAt(string, '.', 0)
print(string)