# another inefficient way, but still works in 10 seconds.
# the right way would be to remember the stack of letters before the first replacement
# and check the following letters, unstacking while there's a match
def process(line):
    old_len = 0

    while old_len != len(line):
        old_len = len(line)
        for a in range(26):
            repl = chr(a + ord('a')) + chr(a + ord('A'))
            line = line.replace(repl, "")
            repl = chr(a + ord('A')) + chr(a + ord('a'))
            line = line.replace(repl, "")

    return(len(line))

def main():
    file = open("inputs/input5.txt")

    for line in file:

        line = line.strip()
        print(process(line))

        shortest = len(line)
        for i in range(26):
            short = line.replace(chr(i + ord('A')), "")
            short = short.replace(chr(i + ord('a')), "")
            shortest = min(shortest, process(short))
            
        print(shortest)
            

if __name__ == "__main__":
    main()
