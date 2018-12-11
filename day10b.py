import queue
import math
import numpy as np
import copy

def process(points):

    # the big    
    # t = big_a * t ^ 2 + big_b * t + big_c
    big_a = 0
    big_b = 0
    big_c = 0

    # how the center x moves in time cx_a * t + cx_b
    cx_a = 0
    cx_b = 0

    # how the center x moves in time cx_a * t + cx_b
    cy_a = 0
    cy_b = 0

    for it in range(len(points)):
        cx_a = cx_a + points[it][2]
        cy_a = cy_a + points[it][3]

        cx_b = cx_b + points[it][0]
        cy_b = cy_b + points[it][1]

    # the center of mass will have coordinate cx_a * t + cx_b, cy_a * t + cy_b
    cx_a = cx_a / len(points)
    cx_b = cx_b / len(points)
    cy_a = cy_a / len(points)
    cy_b = cy_b / len(points)

    # computes the parameters of the total sum of distance to center of mass as 
    # t = big_a * t ^ 2 + big_b * t + big_c
    for it in range(len(points)):

        a = points[it][2]
        b = points[it][0]

        big_a = big_a + (a - cx_a) * (a - cx_a)
        big_b = big_b + 2 * (a - cx_a) * (b - cx_b)
        big_c = big_c + (b - cx_b) * (b - cx_b)

        a = points[it][3]
        b = points[it][1]

        big_a = big_a + (a - cx_a) * (a - cx_a)
        big_b = big_b + 2 * (a - cx_a) * (b - cx_b)
        big_c = big_c + (b - cx_b) * (b - cx_b)

    # hopefully this round() is not too far off
    print("minimum at: {}".format((-big_b / (2 * big_a))))
    best_time = int(round(-big_b / (2 * big_a)))

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
