print('Enter a number:')
x = input()  # takes input, but forces it to be a string
print('x is type: ')
print(type(x))  # you can check like this
print(x)
print() #blank makes new line

try:
    xint = int(x) # type cast from string to int
    # print('\nint is type: ')  # \n is a special character in most languages reserved for new line
    # more on special "escape sequences" here http://python-ds.com/python-3-escape-sequences
    # print(type(xint))
    print(xint)
except:
    print("failed int cast")

try:
    xfloat = float(x) # type cast from string to int
    # print('\nxfloat is type: ' + str(type(xfloat)))  # get type of xfloat and convert that to a string to print
    print(xfloat)
except:
    print("failed float cast")

try:
    # print("\nxbool:")
    print(bool(xfloat)) #what values make
except:
    print("failed bool cast")


a = 'hello world'
b = '☃'          # snowman
c = 'घङचछज'     # sanskrit

print("\n\t" + b*5) # print new line, a tab, and the string b 4 times
