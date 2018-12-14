import numpy as np

def prepare(array):
    size_y, size_x = array.shape
    pos = []


    for y in range(size_y):
        for x in range(size_x):
            if array[(y,x)] == '^':
                array[(y,x)] = '|'
                pos.append([x,y,0,-1,0])
            if array[(y,x)] == '>':
                array[(y,x)] = '-'
                pos.append([x,y,1,0,0])
            if array[(y,x)] == 'v':
                array[(y,x)] = '|'
                pos.append([x,y,0,1,0])
            if array[(y,x)] == '<':
                array[(y,x)] = '-'
                pos.append([x,y,-1,0,0])
    return pos

def pos_key(pos):
    return 1000 * pos[1] + pos[0]

def handle_dir(p, array):

    current = array[(p[1], p[0])]

    if current == '|' or current == '-':
        return p

    if current == '/':
        p2 = p[:]
        p[2] = -p2[3]
        p[3] = -p2[2]
    elif current == '\\':
        p2 = p[:]
        p[2] = p2[3]
        p[3] = p2[2]
    elif current == '+':
        p2 = p[:]
        step = p[4]
        p[4] = (step + 1) % 3

        if step == 0:
            p[2] = p2[3]
            p[3] = -p2[2]
        if step == 2:
            p[2] = -p2[3]
            p[3] = p2[2]
    else:
        print('"{}"'.format(current))
        assert(False)

    return p

def move(array, pos):
    pos = sorted(pos, key=pos_key)

    for i in range(len(pos)):
        # move cart
        pos[i][0] = pos[i][0] + pos[i][2]
        pos[i][1] = pos[i][1] + pos[i][3]

        pos[i] = handle_dir(pos[i], array)
        
        for j in range(len(pos)):
            if i != j and pos[i][0] == pos[j][0] and pos[i][1] == pos[j][1]:
                return (pos[i][0], pos[i][1])

    return pos

def main():
    file = open("inputs/input13.txt")

    lines = [x.rstrip() for x in file]

    size_x = max([len(l) for l in lines])
    size_y = len(lines)

    for y in range(size_y):
        lines[y] = lines[y] + ' ' * (size_x - len(lines[y]))
        lines[y] = list(lines[y])

    array = np.array(lines)

    pos = prepare(array)

    count = 0

    while(True):
        pos = move(array,pos)
        count = count + 1
        if len(pos) == 2:
            print(pos, count)
            return

    



main()