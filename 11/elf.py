#!/usr/bin/env python3
from math import sqrt

DAY = 11

def main(test=False):
    input_1 = str(DAY) + '/test_input.txt'
    if not test:
        input_1 = str(DAY) + '/input.txt'
    input_file = open(input_1, 'r')
    Lines = dict([line[:-1].split(": ") for line in input_file])
    Lines = {k: str(v).split(" ") for k, v in Lines.items()}
    count_1   = 0
    count_2   = 0

    paths = []
    for line in Lines:
        if test:
            print(line)

    # for path in paths:
    #     if path[-1] == "count":
    #         count_1 += 1

    count_1 = find_out("you","out",Lines)

    print("Part 1: " + str(count_1))

def find_out(start,end,Lines):
    if end in Lines[start]:
        return 1
    else:
        res = 0
        for node in Lines[start]:
            res += find_out(node,end,Lines)
        return res

if __name__ == '__main__':
    main(test=True)
    main()

