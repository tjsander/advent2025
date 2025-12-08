#!/usr/bin/env python3
import re

DAY = 7

def main(test=False, part2=False):
    input_1 = str(DAY) + '/test_input.txt'
    if not test:
        input_1 = str(DAY) + '/input.txt'
    input_file = open(input_1, 'r')
    Lines = list([line[:-1] for line in input_file])
    count_1   = 0
    count_2   = 1

    # rows = []
    beams = []
    beams.append(Lines[0].find('S') )

    for line in Lines:
        if line.find('^') ==  -1:
            continue
        # rows.append(" ".join(line.split()).split(" "))
        splitters = [m.start() for m in re.finditer('\^', line)]
        new_beams = []
        for beam in beams:
            if beam in splitters:
                count_1 += 1
                count_2 += 1
                new_beams.append(beam -1)
                new_beams.append(beam +1)
            else:
                new_beams.append(beam)
        if not part2:
            beams = list(set(new_beams))
        else:
            beams = new_beams
    # count_2 = len(beams)

    if not part2:
        print("Part 1")
        print(count_1)

    if test:
        for line in Lines:
            print (line)

    if part2:
        print("Part 2")
        print(count_2)

if __name__ == '__main__':
    main(test=True)
    main()
    main(test=True, part2=True)
    # main(part2=True)
