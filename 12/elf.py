#!/usr/bin/env python3

DAY = 12

class Present:
    def __init__(self, index, width, height):
        self.index = index
        self.width = width
        self.height = height
        self.size = 0

        self.grid = []
        for y in range(height):
            row = []
            for x in range(width):
                row.append(".")
            self.grid.append(row)

    def populate_grid(self, Input):
        y = 0
        x = 0
        for line in Input[self.index*5 + 1:self.index*5 + 4]:
            for char in line:
                if char == "#":
                    self.grid[y][x] = "#"
                    self.size += 1
                x += 1
            y += 1
            x = 0

    def return_orientations(self):
        orientations = []
        # Original
        orientations.append(self.grid)
        # Rotated 90
        rot_90 = []
        for x in range(self.width):
            row = []
            for y in reversed(range(self.height)):
                row.append(self.grid[y][x])
            rot_90.append(row)
        orientations.append(rot_90)
        # Rotated 180
        rot_180 = []
        for y in reversed(range(self.height)):
            row = []
            for x in reversed(range(self.width)):
                row.append(self.grid[y][x])
            rot_180.append(row)
        orientations.append(rot_180)
        # Rotated 270
        rot_270 = []
        for x in reversed(range(self.width)):
            row = []
            for y in range(self.height):
                row.append(self.grid[y][x])
            rot_270.append(row)
        orientations.append(rot_270)

        return orientations

    def __str__(self):
        string = ""
        for row in self.grid:
            string += "".join(row) + "\n"
        return string


def main(test=False):
    input_1 = str(DAY) + '/test_input.txt'
    if not test:
        input_1 = str(DAY) + '/input.txt'
    input_file = open(input_1, 'r')
    Input = list([line.strip() for line in input_file])

    presents = []
    Puzzles  = []
    for i in range(0,6):
        presents.append(Present(i,3,3))
    for present in presents:
        present.populate_grid(Input)

    for line in Input[30:]:
        Puzzles.append(line.split(": "))
    for puzzle in Puzzles:
        puzzle[1] = [int(p) for p in puzzle[1].split(" ")]

    if test:
        print("Presents:")
        for present in presents:
            print(present)

    if test:
        orient = presents[0].return_orientations()
        for o in orient:
            for p in o:
                print (p)
            print()

    print("Part 1")

    count_1 = 0
    for puzzle in Puzzles:
        x_y = [int(x) for x in puzzle[0].split("x")]
        area = x_y[0]//3 * x_y[1]//3

        present_area = 0
        for index in range(len(puzzle[1])):
            if puzzle[1][index] > 0:
                for _ in range(puzzle[1][index]):
                    # present_area += presents[index].size
                    present_area +=1

        if present_area <= area:
            count_1 += 1
        else:
            print ("ERROR: cannot fit presents in puzzle ")
        print (puzzle)
    print("Count fit: " + str(count_1))

    print("Part 2")


if __name__ == '__main__':
    main(test=True)
    main()
