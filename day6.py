import numpy as np
import copy

def get_neigh(grid, x, y):
    n = set()
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    for i in range(4):
        if x + dx[i] >= 0 and x + dx[i] < grid.shape[0] and y + dy[i] >= 0 and y + dy[i] < grid.shape[1]:
            if grid[(x+dx[i],y+dy[i])] != 0:
                n.add(grid[(x+dx[i],y+dy[i])])

    return n

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

    count = 1
    for l in lines:
        grid[(l[0], l[1])] = count
        count += 1

    grew = True
    while grew:
        grew = False
        grid2 = copy.copy(grid)
        for x in range(size_x):
            for y in range(size_y):
                if grid[(x,y)] == 0:
                    n = get_neigh(grid, x,y)
                    if len(n) == 1:
                        grid2[(x,y)] = next(iter(n))
                        grew = True
        grid = copy.copy(grid2)

    infinites = set()
    for x in range(size_x):
        infinites.add(grid[x,0])
        infinites.add(grid[x,size_y - 1])
    for y in range(size_y):
        infinites.add(grid[0,y])
        infinites.add(grid[size_x - 1,y])

    print(grid, infinites)
    indices, counts = np.unique(grid, return_counts=True)

    best = 0
    for i in range(len(indices)):
        if indices[i] not in infinites:
            if counts[i] > best:
                best = counts[i]

    print(best)     

if __name__ == "__main__":
    main()
