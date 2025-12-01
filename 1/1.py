#!/usr/bin/env python3
import re

INPUT = '1/input.txt'

def main():
    input_file = open(INPUT, 'r')
    Lines = input_file.readlines()

    position = 50
    dial_array = list(range(100))
    count = 0

    for line in Lines:
        line = line.strip()
        left = line[0] == 'L'
        if left:
            position = (position - int(line[1:])) % 100
        else:
            position = (position + int(line[1:])) % 100
        if position == 0:
            count += 1
    print (count)

if __name__ == '__main__':
    main()
