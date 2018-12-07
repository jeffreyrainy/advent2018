import numpy as np
import copy


def main():
    file = open("inputs/input6.txt")

    lines = []
    for line in file:

        line = line.strip()
        line = line.replace(",","")
        line = line.split()
        line = [int(line[1]), int(line[0])]
        lines.append( line)

    size_x = max([l[0] for l in lines]) + 1
    size_y = max([l[1] for l in lines]) + 1

    grid = np.zeros((size_x, size_y), dtype = int)
    dist = np.zeros((size_x, size_y), dtype = int)

    count = 0
    for x in range(size_x):
        for y in range(size_y):
            d = 0
            for i in range(len(lines)):
                d = d + abs(x - lines[i][0]) + abs(y - lines[i][1])
            dist[(x,y)] = d
            if d < 10000:
                count+=1
    print(dist)
    print(count)


                

if __name__ == "__main__":
    main()
