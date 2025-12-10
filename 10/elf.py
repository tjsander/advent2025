#!/usr/bin/env python3
from itertools import combinations

DAY = 10

def main(test=False):
    input_1 = str(DAY) + '/test_input.txt'
    if not test:
        input_1 = str(DAY) + '/input.txt'
    input_file = open(input_1, 'r')
    Lines = list([line.strip().split(" ") for line in input_file])
    count_1   = 0
    count_2   = 0

    assert (string_to_int("[.##.]") == 6)
    assert (button_string_to_int("(3)"  , 4) == 1)
    assert (button_string_to_int("(1,3)", 4) == 5)
    assert (button_string_to_int("(2)"  , 4) == 2)
    assert (button_string_to_int("(2,3)", 4) == 3)
    assert (button_string_to_int("(0,2)", 4) == 10)
    assert (button_string_to_int("(0,1)", 4) == 12)

    print("Part 1")

    for line in Lines:
        if test:
            print(line)
        machine = string_to_int(line[0])
        buttons = []
        spaces  = len(line[0]) - 2
        for i in range (1, len(line)-1):
            buttons.append(button_string_to_int(line[i], spaces))

        output = press_buttons(machine, buttons)
        print("Buttons pressed = " + str(output))
        count_1 += output

    print("Part 1 = " + str(count_1))

def press_buttons(machine, buttons):
    if machine == 0:
        return 0
    if machine in buttons:
        return 1
    for i in range (2, len(buttons)+1):
        combos = list(combinations(buttons,i))
        for combo in combos:
            output = 0
            for button in combo:
                output = output ^ button
            if output == machine:
                return i
    return -1

def string_to_int(string):
    """.##. -> 6"""
    string = string[1:-1]
    binary_string = string.replace(".", "0").replace("#", "1")
    return int(binary_string, 2)

def button_string_to_int(string, size):
    """(1,3) -> 5"""
    string = string[1:-1]
    parts = string.split(",")
    binary_string = "0" * (size)
    for part in parts:
        binary_string = binary_string[:int(part)] + "1" + binary_string[int(part)+1:]
    return int(binary_string, 2)


if __name__ == '__main__':
    main(test=True)
    main()
