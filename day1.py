import queue
import math
import numpy as np

# note: input was search and replaced to remove plusses

def main():
    file = open("input1.txt")
    mylist = []

    for l in file:
        line = l.strip()
        mylist.append(int(line))

    print(np.sum(mylist))

if __name__ == "__main__":
    main()
