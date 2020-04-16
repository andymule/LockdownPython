import time

def a():
    return 1, 2, 3, "asd"


q, w, e, r = a()
print('asd')
print("asd")

print("\"\"")
print('""')

for _ in range(0,100):
    for i in range(0, 10):
        print("a"*i)
        time.sleep(.03)
    for i in range(10, 0, -1):
        print("a"*i)
        time.sleep(.03)
