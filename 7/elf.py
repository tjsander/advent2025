#!/usr/bin/env python3
import re

DAY = 7

def main(test=False):
    input_1 = str(DAY) + '/test_input.txt'
    if not test:
        input_1 = str(DAY) + '/input.txt'
    input_file = open(input_1, 'r')
    Lines = list([line[:-1] for line in input_file])
    count_1   = 0

    beams = []
    beams.append(Lines[0].find('S') )

    for line in Lines:
        if line.find('^') ==  -1:
            continue

        splitters = [m.start() for m in re.finditer('\^', line)]
        new_beams = []
        for beam in beams:
            if beam in splitters:
                count_1 += 1
                new_beams.append(beam -1)
                new_beams.append(beam +1)
            else:
                new_beams.append(beam)
        beams = list(set(new_beams))

    print("Part 1")
    print(count_1)

    beams_pt2 = []
    for i in range(len(Lines[0])):
        beams_pt2.append(0)
    beams_pt2[Lines[0].find('S')] += 1

    for line in Lines:
        if line.find('^') ==  -1:
            continue

        splitters = [m.start() for m in re.finditer('\^', line)]
        new_beams = []
        for i in range(0,len(beams_pt2)):
            if i in splitters:
                beams_pt2[i-1] += beams_pt2[i]
                beams_pt2[i+1] += beams_pt2[i]
                beams_pt2[i] = 0
        # beams = list(set(new_beams))


    print("Part 2")
    print(sum(beams_pt2))

if __name__ == '__main__':
    main(test=True)
    main()
