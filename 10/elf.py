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
        if test:
            print("Buttons pressed = " + str(output))
        count_1 += output
    print("Part 1 = " + str(count_1))

    print("Part 2")
    for line in Lines:
        if test:
            print(line)
        machine = string_to_int_pt2(line[-1])
        buttons = []
        spaces  = len(line[0]) - 2
        for i in range (1, len(line)-1):
            buttons.append(button_string_to_int(line[i], spaces))

        output = press_buttons_pt2(machine, buttons, line[-1][1:-1].split(","))
        if test:
            print("Buttons pressed = " + str(output))
        count_2 += output

    print("Part 2 = " + str(count_2))

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

def string_to_int_pt2(string):
    """{3,5,4,7} -> 59"""
    target = 0
    mult = 1
    int_array = string[1:-1].split(",")
    for i in reversed(int_array):
        target += int(i) * mult
        mult = mult * 2
    return target

def press_buttons_pt2(machine, buttons, machine_string):
    if machine == 0:
        return 0
    if machine in buttons:
        return 1

    machine_arr = [int(x) for x in machine_string]

    machine_min = min(machine_arr)
    machine_max = max(machine_arr)

    new_buttons = []

    for button in buttons:
        max_button = get_button_max(button, machine_arr)
        for i in range (max_button):
            new_buttons.append(button)

    for i in range (machine_max, sum(buttons)+1):
        for button in buttons:
            mult = machine_max // button
        combos = combinations(new_buttons,i)

        print("Trying " + str(i) + " buttons")
        # print("Combos = " + str(len((combos))))

        for combo in combos:
            if sum(combo) == machine:
                if check_strings_pt2(machine_string, combo):
                    return i
    return -1

def get_button_max(button, machine_arr):
    format_string = '{0:0' + str(len(machine_arr)) + 'b}'
    binary_str = format_string.format(button)
    out_arr = []
    for i in range(len(binary_str)):
        if binary_str[i] == "1":
            out_arr.append(machine_arr[i])
    return min(out_arr)

def check_strings_pt2(machine_string, combo):
    machine_arr = [int(x) for x in machine_string]
    combo_arr = []
    for button in combo:
        format_string = '{0:0' + str(len(machine_arr)) + 'b}'
        binary_str = format_string.format(button)
        button_arr = []
        for i in range(len(binary_str)):
            if binary_str[i] == "1":
                button_arr.append(1)
            else:
                button_arr.append(0)
        combo_arr.append(button_arr)

    summed = []
    for i in range(len(machine_arr)):
        summ = 0
        for arr in combo_arr:
            summ += arr[i]
        summed.append(summ)

    for i in range(len(machine_arr)):
        if summed[i] != machine_arr[i]:
            return False
    return True

if __name__ == '__main__':
    main(test=True)
    main()
