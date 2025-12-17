#!/usr/bin/env python3
import re
from math import prod

DAY = 9

class Area:
    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b
        self.left  = min(point_a[0], point_b[0])
        self.right = max(point_a[0], point_b[0])
        self.top   = min(point_a[1], point_b[1])
        self.bottom= max(point_a[1], point_b[1])
        self.area = (abs(point_a[0]-point_b[0])+1) * (abs(point_a[1]-point_b[1])+1)

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
    Areas = []
    Edges = []

    for point1 in Points:
        for point2 in Points:

            area = find_area(point1, point2)
            if test:
                print (str(point1) + str(point2))
                print (area)

            area_arr.append((area, point1, point2))
            Areas.append(Area(point1, point2))

            if area > biggest_area:

                biggest_area = area
                biggest_1 = point1
                biggest_2 = point2

    for x in range (0,len(Points)-1):
        Edges.append(Area(Points[x], Points[x+1]))
    Edges.append(Area(Points[0], Points[-1]))

    area_arr = sorted(area_arr, key=lambda x: x[0], reverse=True)

    print("Part 1")
    print(biggest_area)
    print(biggest_1)
    print(biggest_2)

    print("Part 2")

    Areas.sort(key=lambda x: x.area, reverse=True)
    for Area1 in Areas:
        collided = False
        for Edge in Edges:
            if Area1 == Edge:
                continue
            if checkAABBCollision(Area1, Edge):
                if test:
                    print("Collision:")
                    print(" Area: " + str(Area1.point_a) + " to " + str(Area1.point_b))
                    print(" Edge: " + str(Edge.point_a) + " to " + str(Edge.point_b))
                collided = True
                break
        if collided:
            continue
        print("No collisions for Area: " + str(Area1.point_a) + " to " + str(Area1.point_b))
        print("Area==: " + str(Area1.area))
        break


def checkAABBCollision(A, B) -> Area:
    AisToTheRightofB = A.left >= B.right
    AisToTheLeftofB  = A.right <= B.left
    AisAboveB        = A.bottom <= B.top
    AisBelowB        = A.top >= B.bottom
    return not (AisToTheRightofB
      or AisToTheLeftofB
      or AisAboveB
      or AisBelowB)

def find_area(point_a, point_b):
    area = (abs(point_a[0]-point_b[0])+1,abs(point_a[1]-point_b[1])+1)
    return prod(area)

if __name__ == '__main__':
    main(test=True)
    main()
