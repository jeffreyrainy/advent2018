import queue
import math
import numpy as np
import string
import re

def main():
    file = open("inputs/input3.txt")

    for line in file:
        line = line.strip()
        line = line.replace('x',' ')
        line = re.findall(r"[\w']+", line)
        print(line)

if __name__ == "__main__":
    main()
