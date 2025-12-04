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
    # check_array(array)
    count = 0
    for y in range(0,len(y_array)):
        for x in range(0,len(y_array[0])):
            if check_roll(y_array, y, x) == 1:
                if (check_access(y_array, y, x) == 1):
                    count += 1
    return count

def check_array_2(y_array):
    # check_array(array)
    count = 0
    for y in range(0,len(y_array)):
        for x in range(0,len(y_array[0])):
            if check_roll(y_array, y, x) == 1:
                if (check_access(y_array, y, x) == 1):
                    count += 1
                    y_array[y][x] = 'x'
    if count == 0:
        return 0
    else:
        final_count = count + check_array_2(y_array)
        return final_count


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
        print("Access Granted at ", y, x)
        return 1
    return 0


if __name__ == '__main__':
    main()
