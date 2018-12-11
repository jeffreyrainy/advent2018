import queue
import math
import numpy as np
import copy

def process(points):
    p = copy.copy(points)
    best = None

    for step in range(20000):
        for it in range(len(p)):
            p[it] = [p[it][0] + p[it][2], p[it][1] + p[it][3], p[it][2], p[it][3]]

        mins = (min(p[:,0]), min(p[:,1]))
        maxs = (max(p[:,0]), max(p[:,1]))

        rx = maxs[0] - mins[0] + 1
        ry = maxs[1] - mins[1] + 1

        if best == None or rx * ry < best:

            best = rx * ry
            best_time = step + 1

    p = copy.copy(points)
    for it in range(len(p)):
        p[it] = [p[it][0] + p[it][2] * best_time, p[it][1] + p[it][3] * best_time, p[it][2], p[it][3]]

    print(best_time)
    return p

def render(p):
    mins = (min(p[:,0]), min(p[:,1]))
    maxs = (max(p[:,0]), max(p[:,1]))

    rx = maxs[0] - mins[0] + 1
    ry = maxs[1] - mins[1] + 1
    pos = set()
    
    for i in range(p.shape[0]):
        pos.add((p[i][0] - mins[0], p[i][1] - mins[1]))
        pass

    for y in range(ry):
        s = ""
        for x in range(rx):
            if (x,y) in pos:
                s = s + "#"
            else:
                s = s + " "
        print(s)

def main():
    file = open("inputs/input10.txt")

    points = []

    for line in file:
        line = line.replace("<", " ")
        line = line.replace(">", " ")
        line = line.replace(",", " ")

        line = line.split()
        line = [line[1], line[2], line[4], line[5]]
        line = [int(x) for x in line]

        points.append(line)
    points = np.array(points) 
    points = process(points)

    render(points)



    

if __name__ == "__main__":
    main()
