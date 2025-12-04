#!/usr/bin/env python3

DAY = 4
INPUT = str(DAY) + '/input.txt'
# INPUT = str(DAY) + '/test_input.txt'

def main():
    input_file = open(INPUT, 'r')
    Lines = (line.rstrip() for line in input_file)
    Lines = list(line for line in Lines if line)

    count_1   = 0
    count_2   = 0

    y_array = []

    for line in Lines:
        horizontal = []
        for char in line:
            horizontal.append(char)
            # print(char)
        # print(horizontal)
        y_array.append(horizontal)


    count_1 = check_array_1(y_array)
    count_2 = check_array_2(y_array)

    # print (y_array)
    print("Part 1")
    print(count_1)
    print("Part 2")
    print(count_2)


def check_array_1(y_array):
    return process_array(y_array, mark=False)

def check_array_2(y_array):
    # Iteratively mark and count until no more matches (avoid recursion)
    total = 0
    while True:
        c = process_array(y_array, mark=True)
        if c == 0:
            break
        total += c
    return total


def process_array(y_array, mark=False):
    """Scan the array for roll characters and, if `mark` is True, mark
    matched cells with 'x'. Returns the number of matches found in one pass.
    """
    count = 0
    height = len(y_array)
    width = len(y_array[0]) if height else 0

    for y in range(height):
        for x in range(width):
            if check_roll(y_array, y, x) == 1:
                if check_access(y_array, y, x) == 1:
                    count += 1
                    if mark:
                        y_array[y][x] = 'x'
    return count


def check_roll(array, y, x):
    if array[y][x] == '@':
        return 1
    return 0

def check_access(array, y, x):
    length = len(array)
    count = 0

    range_y = list(range(y-1, y+2))
    range_x = list(range(x-1, x+2))

    if -1 in range_y: range_y.remove(-1)
    if -1 in range_x: range_x.remove(-1)
    if length in range_y: range_y.remove(length)
    if length in range_x: range_x.remove(length)

    for ry in range_y:
        for rx in range_x:
            count += check_roll(array, ry, rx)

    if count < 5:
        # print("Access Granted at ", y, x)
        return 1
    return 0


if __name__ == '__main__':
    main()
