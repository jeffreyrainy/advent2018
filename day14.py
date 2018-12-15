import numpy as np
from collections import deque

def deque_str(d):
    ret = ""
    l = len(d)
    for i in range(l):
        value = d.popleft()
        ret += str(value) + " "
        d.append(value)

    return ret

def main():
    file = open("inputs/input14.txt")

    value = int(file.readline().strip())

    print(value)

    recipes = deque()
    recipes.append(3)
    recipes.append(7)

    elves = [0,1]

    while True:
        sum = recipes[elves[0]] + recipes[elves[1]]

        if sum > 9:
            recipes.append(sum // 10)
            sum -= 10
        recipes.append(sum)

        elves[0] = (elves[0] + recipes[elves[0]] + 1) % len(recipes)
        elves[1] = (elves[1] + recipes[elves[1]] + 1) % len(recipes)
        
        if len(recipes) > value + 10:
            for i in range(value, value + 10):
                print(recipes[i],end='')
            return

        




main()