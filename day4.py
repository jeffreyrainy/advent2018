import numpy as np

def main():
    file = open("inputs/input4.txt")

    entries = {}
    guards = 0 # number of guards (well, 1 + max id)

    for line in file:
        # read lines
        line = line.strip()
        line = line.replace('[',' ')
        line = line.replace('-',' ')
        line = line.replace(']',' ')
        line = line.replace(':',' ')
        line = line.replace('#',' ')
        line = line.split()
        when = int(line[0]) * 100000000 + int(line[1]) * 1000000 + int(line[2]) * 10000 + int(line[3]) * 100 + int(line[4])

        # check that we don't have multiple event at the same time
        assert(not when in entries)

        # keep track of largest guard id plus one
        if line[5] == "Guard":
            guards = max(guards, int(line[6]) + 1)
        entries[when] = line[3:]

    # we'll simply count how often each guard sleeps at each minute
    minutes_slept = np.zeros((guards, 60))

    awake = True
    for k in sorted(entries.keys()):

        hours, minutes, action = int(entries[k][0]), int(entries[k][1]), entries[k][2]

        if action == "Guard":
            # check that previous guard ended the day awake
            assert(awake)
            guard = int(entries[k][3])

        elif action == "falls":
            sleep_time = minutes
            awake = False

        elif action == "wakes":
            wake_time = minutes
            awake = True
            for t in range(sleep_time, wake_time):
                minutes_slept[(guard, t)] += 1

    # check that last guard ended the day awake
    assert(awake)

    sleepiest_guard = minutes_slept.sum(axis=1).argmax()
    sleepiest_minute = minutes_slept[sleepiest_guard].argmax()

    print(sleepiest_guard * sleepiest_minute)
    (guard, minute) = np.unravel_index(np.argmax(minutes_slept), minutes_slept.shape)
    print(guard * minute)


if __name__ == "__main__":
    main()
