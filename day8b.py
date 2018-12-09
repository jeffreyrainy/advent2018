import queue
import math
import numpy as np

total = 0

def process(inputs):
    global total

    my_value = 0
    children_values = []

    nb = inputs[0]
    meta = inputs[1]
    inputs = inputs[2:]

    for i in range(nb):
        inputs, value = process(inputs)
        children_values.append(value)

    metas = inputs[0:meta]

    total = total + sum(metas)

    if nb:
        for i in metas:
            if i > 0 and i <= len(children_values):
                my_value += children_values[i - 1]
    else:
        my_value = sum(metas)

    inputs = inputs[meta:]

    return inputs, my_value

def main():
    file = open("inputs/input8.txt")
        
    inputs = file.readline().strip().split()
    inputs = [int(v) for v in inputs]
    print(process(inputs))

    print(total)    




if __name__ == "__main__":
    main()
