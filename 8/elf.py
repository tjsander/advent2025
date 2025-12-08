#!/usr/bin/env python3
from math import sqrt

DAY = 8

def main(test=False, no_connections=10):
    input_1 = str(DAY) + '/test_input.txt'
    if not test:
        input_1 = str(DAY) + '/input.txt'
    input_file = open(input_1, 'r')
    Lines = list([[int(i) for i in line.strip().split(",")] for line in input_file])
    count_1   = 0
    count_2   = 0

    node_distances = []

    for line_a in Lines:
        for line_b in Lines:
            if line_a == line_b:
                continue
            distance_a_b = distance(line_a, line_b)
            node_distances.append((distance_a_b, line_a, line_b))

    node_distances.sort(key=lambda x: x[0])
    new_distances = []
    for i in range (len(node_distances)):
        if i % 2 == 0:
            new_distances.append(node_distances[i])

    connections = make_connections(new_distances, no_connections)
    print("Part 1")
    connection_lengths = [len(connection) for connection in connections]
    connection_lengths.sort(reverse=True)
    print(connection_lengths[0]*connection_lengths[1]*connection_lengths[2])

    print("Part 2")
    count_2 = make_connections_forever(new_distances, Lines)
    print(count_2)

def make_connections_forever(node_distances, nodes):
    connections = []
    count = 0

    i = 0
    while i < len(node_distances):

        node_a = node_distances[i][1]
        node_b = node_distances[i][2]

        if len(connections) == 0:
            connections.append([node_a, node_b])
            i += 1
            continue
        merged = False
        for connection in connections:
            if node_a in connection and node_b in connection:
                merged = True
                break
            if node_a in connection:
                if node_b not in connection:
                    connection.append(node_b)
                    merged = True
                    break
            if node_b in connection:
                if node_a not in connection:
                    connection.append(node_a)
                    merged = True
                    break
        if not merged:
            connections.append([node_a, node_b])
        i += 1

        finished = False
        while not finished:
            connections, finished = merge_connections(connections)
        if (len(connections[0])== len(nodes)):
            return node_a[0] * node_b[0]
        continue
    return -1

def make_connections(node_distances, size_limit):
    connections = []
    count = 0

    i = 0
    while i < size_limit:

        node_a = node_distances[i][1]
        node_b = node_distances[i][2]

        if len(connections) == 0:
            connections.append([node_a, node_b])
            i += 1
            continue
        merged = False
        for connection in connections:
            if node_a in connection and node_b in connection:
                merged = True
                break
            if node_a in connection:
                if node_b not in connection:
                    connection.append(node_b)
                    merged = True
                    break
            if node_b in connection:
                if node_a not in connection:
                    connection.append(node_a)
                    merged = True
                    break
        if not merged:
            connections.append([node_a, node_b])
        i += 1
        continue

    finished = False
    while not finished:
        connections, finished = merge_connections(connections)

    return connections

def merge_connections(connections):
    merged = False
    ever_merged = False
    for connection1 in connections:
        for connection2 in connections:
            if connection1 == connection2:
                continue
            for node in connection2:
                if node in connection1:
                    for node_to_add in connection2:
                        if node_to_add not in connection1:
                            connection1.append(node_to_add)
                    merged = True
                    ever_merged = True

            if merged:
                connections.remove(connection2)
                merged = False
                break
    return connections, not ever_merged

def distance (a, b):
    return sqrt((abs(a[0] - b[0])**2) + (abs(a[1] - b[1])**2) + (abs(a[2] - b[2])**2))

if __name__ == '__main__':
    main(test=True, no_connections=10)
    main(no_connections=1000)

# 8280 too low...
# 18354 not right
