#!/usr/bin/env python3

DAY = 3
INPUT = str(DAY) + '/input.txt'
# INPUT = str(DAY) + '/test_input.txt'

def main():
    input_file = open(INPUT, 'r')
    Lines = (line.rstrip() for line in input_file)
    Lines = list(line for line in Lines if line)

    count_1   = 0
    count_1_2 = 0
    count_2   = 0

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
        count_1 += max(left_max, right_max)

    # Verification that part 2 works correctly

    for line in Lines:
        max_jolt = int(part2_recursive(line, 2))
        count_1_2 += max_jolt



    for line in Lines:
        max_jolt = int(part2_recursive(line, 12))
        count_2 += max_jolt

    print("Part 1")
    print(count_1)
    print("Part 2 Verification")
    print(count_1_2)
    print("Part 2")
    print(count_2)

def part2_recursive(input_string, JOLT_SIZE):
    """
    Find the largest number in the remaining string that still enough remaining digits to satisfy JOLT_SIZE
    """
    output_string = ""
    finished = False
    max_capacity = (max(map(int, input_string)))
    if (JOLT_SIZE == 1):
        return str(max_capacity)
    while (max_capacity > 0):
        max_idx = input_string.find(str(max_capacity))
        if (max_idx != -1):
            if (len(input_string[max_idx:]) >= JOLT_SIZE):
                output_string += str(max_capacity)
                output_string += str(part2_recursive(input_string[max_idx+1:], JOLT_SIZE-1))
                return output_string
        max_capacity -= 1
    return -1

def remove_at(i: int, s: str) -> str:
    return s[:i] + s[i+1:]

if __name__ == '__main__':
    main()
