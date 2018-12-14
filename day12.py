import numpy as np

def trim(value, pos):

    i = 0
    while value[i] == '.':
        i += 1
        pos += 1
    value = value[i:]

    i = -1
    if value[i] == '.':
        while value[i] == '.':
            i -= 1
        value = value[:i+1]

    return value, pos

def process(it, tape, rules, left):
    tape = ['.', '.', '.'] + tape + ['.', '.', '.']
    left -= 3
    ret = tape[:]

    for i in range(2, len(tape) - 2):
        key = ''.join(tape[i - 2: i + 3])
        if key in rules:
            ret[i] = rules[key]

    ret, left = trim(ret,left)
    return ret, left

def run(tape, rules):
    left = 0
    iterations = 50000000000
    predicted = False

    for i in range(iterations):
        prev, prev_left = tape[:], left
        tape, left = process(i, tape, rules, left)

        if not predicted and prev == tape:
            pred_left = left + (iterations - i) * (left - prev_left) - 1

            print("Same value again. i is {}, shift is {}, predicted shift is {} ".format(i,left - prev_left, pred_left))
            predicted = True
            break

    if predicted:
        left = pred_left
    count = 0
    for x in range(len(tape)):
        if tape[x] == '#':
            count += (x + left)

    print(count)

def main():
    global do_trim
    file = open("inputs/input12.txt")

    tape = list(file.readline().split()[2])
    rules = {}

    for line in file:
        line = line.split()
        if len(line):
            pattern, result = line[0], line[2]
            rules[pattern] = result

    run(tape, rules)


if __name__ == "__main__":
    main()
