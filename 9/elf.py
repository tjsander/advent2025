#!/usr/bin/env python3
import re
from math import prod

DAY = 9

class Grid:
    def __init__(self, points):
        self.points = points
        self.width = 1
        self.height = 1
        self.grid = []
        self.y_dict = None
        self.x_dict = None
        self.build_simple_grid()

    def is_red_or_green(point):
        return False

    def add_point(self, point):
        return -1

    def build_simple_grid(self):
        x_set = set()
        y_set = set()
        for point in self.points:
            x_set.add(point[0])
            y_set.add(point[1])


        self.x_dict = {v: k for k, v in enumerate(sorted(x_set))}
        self.y_dict = {v: k for k, v in enumerate(sorted(y_set))}

        self.width  = len(self.x_dict)
        self.height = len(self.y_dict)

        for y in range(self.height):
            row = []
            for x in range(self.width):
                row.append(".")
            self.grid.append(row)

        return True

    def __str__(self):
        string = ""
        for row in self.grid:
            string += "".join(row) + "\n"
        return string

class Point:
    def __init__(self, x, y, color="."):
        self.x = x
        self.y = y
        self.color = color


def main(test=False):
    input_1 = str(DAY) + '/test_input.txt'
    if not test:
        input_1 = str(DAY) + '/input.txt'
    input_file = open(input_1, 'r')
    Points = list([line.strip().split(",") for line in input_file])
    Points = [ [int(x[0]), int(x[1])] for x in Points ]

    biggest_1 = (0,0)
    biggest_2 = (0,0)
    biggest_area = 0

    area_arr = []
    for point1 in Points:
        for point2 in Points:

            area = find_area(point1, point2)
            if test:
                print (str(point1) + str(point2))
                print (area)

            area_arr.append((area, point1, point2))

            if area > biggest_area:

                biggest_area = area
                biggest_1 = point1
                biggest_2 = point2

    area_arr = sorted(area_arr, key=lambda x: x[0], reverse=True)

    print("Part 1")
    print(biggest_area)
    print(biggest_1)
    print(biggest_2)

    print("Part 2")
    grid = Grid(Points)
    print(str(grid))

def find_area(point_a, point_b):
    area = (abs(point_a[0]-point_b[0])+1,abs(point_a[1]-point_b[1])+1)
    return prod(area)

if __name__ == '__main__':
    main(test=True)
    # main()
