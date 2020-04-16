import random

random.seed(1337)  # seed determines what numbers come out, lets us make reproducible randomness
mylist = [int(random.random() * 10) for _ in range(0, 10)]  # list of 10 random ints
charlist = [chr(int(random.random() * 26 + 64)) for _ in range(0, 10)]  # list of 10 random characters
#####  You haven't learned the stuff above here, but you should/will soon know all things below here #####

# Debug step thru all this stuff

print(sum(mylist))  # total value of all items summed
print(mylist.count(3))  # how many 3s in mylist
print(mylist.count(3) > 0)  # is 3 in the list?
print(3 in mylist)  # same as above, but written better, aka do it this way
print(sum(mylist) / len(mylist))  # average entry of list
print(mylist.index(3))  # first location of 3 in the list
print(mylist[mylist.index(3)])  # should return 3 because we're using its index directly

mylist.append(69)
lastnumber = mylist[-1]  # save last item
mylist = mylist[:-1]  # remove last item in list

mylist.append(69)
lastnumber = mylist.pop()  # removes and returns last item in list, same as above code

mylist.sort()
mylist.reverse()
mylist.sort(reverse=True)  # same as two lines above
mylist = sorted(mylist, reverse=True)  # also same result as line above

dumb = not not not not not True
print(dumb)

bothlists = list(zip(mylist, charlist))  # combine two lists into a joint list of both
print(bothlists[0])  # first item
print(bothlists[-1])  # last item

allchar = ""
allnums = ""
for num, char in zip(mylist, charlist):  # zip really makes this "iterable"
    # we can access any iterable like a list or string
    allnums += str(num)
    allchar += char  # already string

print(allnums + allchar)

pass  # does nothing, is a placeholder
