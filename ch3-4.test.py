import random
import sys
import traceback

random.seed(0xDEAD)  # seed determines what numbers come out, lets us make reproducible randomness
numlist = [int(random.random() * 1000) for _ in range(0, 1000)]  # list of 1000 random ints
charlist = [chr(int(random.random() * 26 + 64)) for _ in range(0, 1000)]  # list of 1000 random characters


#####  You haven't learned the stuff above here, the test is below this point #####


def howMany69(mylist):
    # TODO write a function that returns the number of 69s in the input list
    pass


def whereIs69(mylist):
    # TODO write a function that returns the first index of 69 in the input list
    pass


def averageFirstHalfOfList(mylist):
    # TODO write a function that averages the first half of the input list
    pass


def countO(mylist):
    # TODO write a function that averages the first half of the input list
    pass


# challenge! might take some googling
def sortReverse10string(mylist):
    # TODO write a function that sorts an input list, reverses it, keeps the first ten elements, and returns those in a string 
    pass


########  below here checks your answers for you ##########################

try:
    assert (howMany69(numlist) == 2), "howMany69 is wrong!"
    assert (whereIs69(numlist) == 510), "whereIs69 is wrong!"
    assert (averageFirstHalfOfList(numlist) == 498.992), "averageFirstHalfOfList is wrong!"
    assert (countO(charlist) == 41), "countO is wrong!"
    assert (sortReverse10string(charlist) == "YYYYYYYYYY"), "sortReverse10string is wrong!"
    print("YOU DID IT ALL NICELY WOW")
except AssertionError:
    _, _, tb = sys.exc_info()
    traceback.print_tb(tb)  # Fixed format
    tb_info = traceback.extract_tb(tb)
    filename, line, func, text = tb_info[-1]

