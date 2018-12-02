import queue
import math
import numpy as np

def match(a,b):
    count = 0
    out = ""
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    if count != 1:
        return False

    for i in range(len(a)):
        if a[i] == b[i]:
            out = out + a[i]  
    print(out)
    return True

def main():
    file = open("inputs/input2.txt")

    lines =  []
    for line in file:
        line = line.strip()
        lines.append(line)

    for i in lines:
        for j in lines:
            if i != j and match(i,j):
                return

if __name__ == "__main__":
    main()
