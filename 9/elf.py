#!/usr/bin/env python3
import re
from math import prod

DAY = 9

def main(test=False):
    input_1 = str(DAY) + '/test_input.txt'
    if not test:
        input_1 = str(DAY) + '/input.txt'
    input_file = open(input_1, 'r')
    Lines = list([line.strip().split(",") for line in input_file])
    Lines = [ [int(x[0]), int(x[1])] for x in Lines ]

    biggest_1 = (0,0)
    biggest_2 = (0,0)
    biggest_area = 0

    for line in Lines:
        for line2 in Lines:
            print (str(line) + str(line2))
            area = find_area(line, line2)
            print (area)
            if area > biggest_area:
                biggest_area = area
                biggest_1 = line
                biggest_2 = line2

    print("Part 1")
    print(biggest_area)
    print(biggest_1)
    print(biggest_2)

    print("Part 2")
    # print(sum(beams_pt2))

def find_area(point_a, point_b):
    area = (abs(point_a[0]-point_b[0])+1,abs(point_a[1]-point_b[1])+1)
    return prod(area)

if __name__ == '__main__':
    main(test=True)
    main()
