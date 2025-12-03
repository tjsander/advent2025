#!/usr/bin/env python3
import re
import textwrap

DAY = 2
INPUT = str(DAY) + '/input.txt'
# INPUT = str(DAY) + '/test_input.txt'

def main():
    input_file = open(INPUT, 'r')
    Lines = input_file.readlines()

    count_1 = 0
    count_2 = 0

    ranges = Lines[0].strip().split(',')

    for line in ranges:
        ran = line.split('-')
        start = int(ran[0])
        end = int(ran[1])
        range_arr = range(start,end+1)
        for i in range_arr:
            if is_invalid(str(i)):
                count_1 += int(i)
            if is_invalid_pt_2(str(i)):
                count_2 += int(i)

    print(count_1)
    print(count_2)

def is_invalid(input_string):
    if len(input_string) %2 != 0:
        return False

    length = len(input_string) // 2

    first_half  = input_string[:length]
    second_half = input_string[length:]

    if first_half == second_half:
        return True

    return False

def is_invalid_pt_2(input_string):
    length = len(input_string)

    # for i in reversed(range (1, length//2 +1) ):
    for i in range(1, length//2 +1):
        if length % i != 0:
            continue

        num_array = textwrap.wrap(input_string, i)

        all_equal = all(x == num_array[0] for x in num_array)
        if all_equal:
            return True

    return False

if __name__ == '__main__':
    main()
