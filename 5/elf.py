#!/usr/bin/env python3

DAY = 5
INPUT = str(DAY) + '/input.txt'
INPUT2 = str(DAY) + '/input_2.txt'

# INPUT = str(DAY) + '/test_input.txt'
# INPUT2 = str(DAY) + '/test_input_2.txt'

def main():
    input_file = open(INPUT, 'r')
    Ranges = (line.rstrip() for line in input_file)
    Ranges = list(line for line in Ranges if line)

    input_file2 = open(INPUT2, 'r')
    IDs = (line.rstrip() for line in input_file2)
    IDs = list(line for line in IDs if line)

    count_1   = 0
    count_2   = 0

    y_array = []

    for ident in IDs:
        for rng in Ranges:
            if int(ident) in range(int(rng.split('-')[0]), int(rng.split('-')[1])):
                count_1 += 1
                break

    print("Part 1")
    print(count_1)
    print("Part 2")
    print(count_2)

if __name__ == '__main__':
    main()
