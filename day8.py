import queue
import math
import numpy as np

total = 0

def process(inputs):
    global total

    nb = inputs[0]
    meta = inputs[1]
    inputs = inputs[2:]

    for i in range(nb):
        inputs = process(inputs)
    
    metas = inputs[0:meta]
    inputs = inputs[meta:]

    total = total + sum(metas)

    return inputs

def main():
    file = open("inputs/input8.txt")
        
    inputs = file.readline().strip().split()
    inputs = [int(v) for v in inputs]
    process(inputs)    

    print(total)    




if __name__ == "__main__":
    main()
