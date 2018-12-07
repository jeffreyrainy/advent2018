import queue
import math
import numpy as np
import queue

extra = 60
workers = 5

def main():
    file = open("inputs/input7.txt")

    prereq = {}

    for line in file:
        line = line.strip().split()
        a, b = line[1], line[7]

        if not a in prereq:
            prereq[a] = []
        if not b in prereq:
            prereq[b] = []

        prereq[b].append(a)


    now = 0
    available = [i for i in range(workers)]

    q = queue.PriorityQueue()

    while prereq and len(prereq) != 0:
        picked = None
        while not picked:
            for k in sorted(prereq.keys()):
                v = prereq[k]
                if not v or len(v) == 0:
                    picked = k
                    break
            
            if not picked:
                ###
                (next, (worker, done)) = q.get()
                available.append(worker)
                now = next
                print(now)
                ###

                for k,v in prereq.items():
                    if v and done in v:
                        prereq[k].remove(done)

            if not prereq or not len(prereq):
                break

            if len(available) == 0:
                ###
                (next, (worker, done)) = q.get()
                available.append(worker)
                now = next
                print(now)
                ###

                for k,v in prereq.items():
                    if v and done in v:
                        prereq[k].remove(done)

        worker = available[0]
        available = available[1:]

        print("worker {} picks {} at {}".format(worker, picked, now))
        q.put(((now + extra + 1 + ord(picked) - ord('A')), (worker, picked)))
        del prereq[picked]

    while not q.empty():
        (next, (worker, done)) = q.get()
        available.append(worker)
        now = next
        print(now)


        




if __name__ == "__main__":
    main()
