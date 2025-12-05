#!/usr/bin/env python3
from itertools import chain

DAY = 5
INPUT = str(DAY) + '/input.txt'
INPUT2 = str(DAY) + '/input_2.txt'

# INPUT = str(DAY) + '/test_input.txt'
# INPUT2 = str(DAY) + '/test_input_2.txt'

def main():
    input_file = open(INPUT, 'r')
    Ranges = (line.rstrip() for line in input_file)
    Ranges = list(range(int(line.split('-')[0]), int(line.split('-')[1])+1) for line in Ranges if line)

    input_file2 = open(INPUT2, 'r')
    IDs = (line.rstrip() for line in input_file2)
    IDs = list(line for line in IDs if line)

    count_1   = 0
    count_2   = 0

    y_array = []

    for ident in IDs:
        for rng in Ranges:
            if int(ident) in rng:
                count_1 += 1
                break

    print("Part 1")
    print(count_1)

    # COMBINE RANGES
    # Ranges.sort(key=lambda rng: rng[0])

    finished = False
    while not finished:
        finished = True
        for rng in Ranges:
            while Ranges.count(rng) > 1:
                Ranges.remove(rng)
            for other_rng in Ranges:
                if rng == other_rng:
                    continue
                if (other_rng[0] >= rng[0] and other_rng[0] <= rng[-1]) or (other_rng[-1] >= rng[0] and other_rng[-1] <= rng[-1]):
                    new_start = min(rng[0], other_rng[0])
                    new_end   = max(rng[-1], other_rng[-1])
                    new_range = range(new_start, new_end+1)
                    Ranges.remove(rng)
                    Ranges.remove(other_rng)
                    Ranges.append(new_range)
                    finished = False
                    break
        Ranges.sort(key=lambda rng: rng[0])

    for rng in Ranges:
        count_2 += len(rng)

    print("Part 2")
    print(count_2)

if __name__ == '__main__':
    main()
