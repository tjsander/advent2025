#!/usr/bin/env python3

DAY = 3
INPUT = str(DAY) + '/input.txt'
# INPUT = str(DAY) + '/test_input.txt'

def main():
    input_file = open(INPUT, 'r')
    Lines = (line.rstrip() for line in input_file)
    Lines = list(line for line in Lines if line)

    count_1 = 0
    count_2 = 0

    for line in Lines:
        # get the largest number in the line
        max_int = (max(map(int, line)))
        max_idx = line.find(str(max_int))

        left_max = 0
        right_max = 0

        # get the largest number to the left
        if max_idx != 0:
            left_part = line[:max_idx]
            left_max = max(map(int, left_part)) if left_part else -1
            left_max = 10 * left_max + max_int

        # get the largest number to the right
        if max_idx != len(line)-1:
            right_part = line[max_idx+1:]
            right_max = max(map(int, right_part)) if right_part else -1
            right_max = 10 * max_int + right_max

        max_max = max(left_max, right_max)
        print(max_max)
        count_1 += max(left_max, right_max)

    print("Part 2")

    for line in Lines:
        max_jolt = part_2(line)
        count_2 += max_jolt


    # 147952302767971 is too low??
    # 170044670732187 also too low.........
    # 169978016428836 also wrong
    # 3031110778619
    # 169059991684173 WRONG
    # 169129168648781 WRONG

    print(count_1)
    print(count_2)

def part_2(input_string):
    JOLT_SIZE = 12
    smallest_int = (min(map(int, input_string)))
    reduced_string = input_string

    # trim the input string
    max_int = (max(map(int, input_string)))

    max_idx = input_string.find(str(max_int))
    if (len(input_string[max_idx:]) >= JOLT_SIZE):
        reduced_string = input_string[max_idx:]

    input_string = reduced_string

    while (smallest_int < max_int):
        input_string = input_string.replace(str(smallest_int), '')
        if (len(input_string) > JOLT_SIZE):
            reduced_string = input_string
            smallest_int += 1
        else:
            break

    delete_index = reduced_string.find(str(smallest_int))

    while (len(reduced_string) > JOLT_SIZE):
        reduced_string = remove_at(delete_index, reduced_string)

        #DELETE ANY NUMBERS THAT ARE LESS THAN THE NEXT NUMBER UNTIL YOU REACH SMALLEST_INT
        # while (reduced_string[delete_index] != str(smallest_int) and
        #        int(reduced_string[delete_index]) < int(reduced_string[delete_index +1])):
        #     reduced_string = remove_at(delete_index, reduced_string)
        while (len(reduced_string) > JOLT_SIZE and delete_index < JOLT_SIZE
            and int(reduced_string[delete_index]) < int(reduced_string[delete_index +1])
            and reduced_string[delete_index] != str(smallest_int)):
            reduced_string = remove_at(delete_index, reduced_string)
        delete_index = reduced_string.find(str(smallest_int))

    print (reduced_string)
    return int(reduced_string)

def remove_at(i: int, s: str) -> str:
    return s[:i] + s[i+1:]

if __name__ == '__main__':
    main()
