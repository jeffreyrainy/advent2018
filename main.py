import queue
import math
import numpy as np

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def process(line):
        print(line)
        print(line.split("."))
        print(line.split())

        list = [ord(c) for c in line]
        line = [chr(x) for x in list]
        line = ''.join(line)
        print(line)

def list_stuff():
    my_list = [7,1,4,2,1,3,5,1]
    my_list.sort()
    print(my_list)

def dict_stuff():
    a = {}
    a["foo"] = "bar"
    a["bar"] = "foo"

    for x,y in a.items():
        print(x,y)

def numpy_stuff():
    a = [[123, 234], [1, 2]]
    b = [915, 718]

    print(np.dot(a,b))

def main():
    file = open("input.txt")
    for l in file:
        line = l.strip()
        process(line)

    s = set()
    s.add(4)
    s.add(4)
    s.add(5.0)
    s.remove(4)
    print(s)

    q = queue.PriorityQueue()
    q.put((2,"two"))
    q.put((1,"one"))
    q.put((3,"three"))

    print("foobar".find("bar"))
    print("foucault".find("bar"))

    while not q.empty():
        print(q.get())

    print(math.sin(3))
    print(max(1,2,3))

    list_stuff()
    dict_stuff()
    numpy_stuff()

if __name__ == "__main__":
    main()
