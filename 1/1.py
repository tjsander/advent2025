#!/usr/bin/env python3
import re

INPUT = '1/input.txt'
# INPUT = '1/test_input.txt'

def main():
    input_file = open(INPUT, 'r')
    Lines = input_file.readlines()

    position = 50
    dial_array = list(range(100))
    count_1 = 0
    count_2 = 0

    for line in Lines:
        line = line.strip()
        left = line[0] == 'L'
        if left:
            initial_position = position
            position = (position - int(line[1:]))
            if position <= 0 and initial_position != 0:
                count_2 += 1
            if position < -99:
                zeroes = int(abs(position)/100)
                count_2 += zeroes
            position = abs(position % 100)

        else:
            position = (position + int(line[1:]))
            zeroes = int(position/100)
            count_2 += zeroes
            position = position % 100

        if position == 0:
            count_1 += 1

    print(count_1)
    print(count_2)

if __name__ == '__main__':
    main()
