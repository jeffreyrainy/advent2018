import numpy as np

def process(sum_corner, r, size):
    best = 0
    for z in range(r[0], r[1]):
        for x in range(size - z):
            for y in range(size - z):
                v = sum_corner[(x + z,y + z)] - sum_corner[x + z, y] - sum_corner[x, y + z] + sum_corner[x, y]

                if v > best:
                    best = v
                    best_coord = (x + 1, y + 1, z)

    print(best_coord)

def main():
    file = open("inputs/input11.txt")

    serial = int(file.readline())
    size = 300

    # the sum from the (0,0) corner to a given position
    sum_corner = np.zeros((size,size), dtype=int)

    for x in range(size):
        for y in range(size):
            v = ((((x + 10) * y + serial) * (x + 10)) // 100) % 10 - 5
            sum_corner[(x,y)] = sum_corner[(x-1,y)] + sum_corner[(x,y - 1)] - sum_corner[(x - 1,y - 1)] + v

    process(sum_corner, [3,4], size)
    process(sum_corner, [0,size], size)



if __name__ == "__main__":
    main()
