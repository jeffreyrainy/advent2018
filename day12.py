import numpy as np

left = 0

def process(tape, rules):
    global left

    if '.' in tape[0:2] or '.' in tape[-2, 0]:
        tape = ['.', '.'] + tape + ['.', '.']
        left -= 2
    ret = tape[:]

    for i in range(2, len(tape) - 2):
        key = ''.join(tape[i - 2: i + 3])
        if key in rules:
            ret[i] = rules[key]

    return ret

def main():
    file = open("inputs/input12.txt")

    tape = list(file.readline().split()[2])
    rules = {}

    for line in file:
        line = line.split()
        if len(line):
            pattern, result = line[0], line[2]
            rules[pattern] = result


    iterations = 20

#    print(''.join(tape))
    for i in range(iterations):
        tape = process(tape, rules)
#        print(''.join(tape))

        if i % 100 == 0:
            print(i)
    count = 0
    for x in range(len(tape)):
        if tape[x] == '#':
            count += (x + left)

    print(count)


if __name__ == "__main__":
    main()
