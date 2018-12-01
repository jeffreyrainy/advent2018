import queue
import math
import numpy as np

def main():
    file = open("inputs/input1.txt")
    mylist = []

    for l in file:
        line = l.strip()
        mylist.append(int(line))

    freq = 0
    freqs = set()

    while True:
        for x in mylist:
            freq = freq + x

            if freq in freqs:
                print(freq)
                return
            freqs.add(freq)

if __name__ == "__main__":
    main()
