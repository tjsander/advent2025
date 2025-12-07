#!/usr/bin/env python3

DAY = 6

def main(test=False):
    input_1 = str(DAY) + '/test_input.txt'
    if not test:
        input_1 = str(DAY) + '/input.txt'
    input_file = open(input_1, 'r')
    Lines = list([line[:-1] for line in input_file])
    count_1   = 0
    count_2   = 0
    rows = []

    for line in Lines:
        rows.append(" ".join(line.split()).split(" "))

    for i in range (0,len(rows[0])):
        if rows[-1][i] == "*":
            product = int(rows[0][i])
            for x in range(1, len(rows)-1):
                product *= int(rows[x][i])
            count_1 += product
            if test:
                print("Product=" + str(product))
        else:
            summ = 0
            for x in range(0, len(rows)-1):
                summ += int(rows[x][i])
            count_1 += summ
            if test:
                print("Sum=" + str(summ))

    print("Part 1")
    print(count_1)


    for line in Lines:
        print (line)

    indexes = []
    operators = []
    for i in range (0,len(Lines[-1])):
        char = Lines[-1][i]
        # print("Char=" + char)
        if char == "*":
            indexes.append(i)
            operators.append("*")
        if char == "+":
            indexes.append(i)
            operators.append("+")
    number_stack = []
    index = 0
    for char_index in range(0, len(Lines[0])):
        number = ""
        for line in Lines[:-1]:
            # number.
            number += (str(line[char_index]))
        number = number.replace(" ", "")
        if number != "":
            number_stack.append(int(number))
            index += 1
        else:
            number_stack.append(-1)
    number_stack.append(-1)
    print(number_stack)
    
    for op in operators:
        if op == "*":
            prod = 1
            while number_stack[0] != -1:
                prod *= number_stack.pop(0)
            number_stack.pop(0)
            count_2 += prod
            if test:
                print("prod=" + str(prod))
        if op == "+":
            summ = 0
            while number_stack[0] != -1:
                summ += number_stack.pop(0)
            number_stack.pop(0)
            if test:
                print("sum=" + str(summ))
            count_2 += summ
        print(op)

            
    print("Part 2")
    if test:
        print(indexes)
        for line in Lines:
            print (str(len(line)))
    print(count_2)

if __name__ == '__main__':
    main(test=True)
    main()
