#!/usr/bin/env python3
from math import sqrt
from functools import cache

DAY = 11
GRAPH = {}

def main(test=False, pt2=False):
    input_1 = str(DAY) + '/test_input.txt'
    if pt2:
        input_1 = str(DAY) + '/test_input_2.txt'
    if not test:
        input_1 = str(DAY) + '/input.txt'
    input_file = open(input_1, 'r')
    Lines = dict([line[:-1].split(": ") for line in input_file])
    Lines = {k: str(v).split(" ") for k, v in Lines.items()}
    count_1   = 0
    count_2   = 0

    if test:
        print("TESTING ====")
    else:
        print("RUNNING ====")

    # build a cleaned, immutable graph and initialize caches
    set_graph(Lines)

    if not pt2:
        count_1 = find_out("you", "out")
        print("Part 1: " + str(count_1))

    if pt2:
        count_1 = find_out("svr", "out")
        print("Part 2 total : " + str(count_1))

        count_2 = find_out2("svr", "out")
        print("Part 2: " + str(count_2))


def set_graph(Lines):
    """Convert the parsed Lines mapping to a stable adjacency mapping
    and clear caches for cached functions.
    """
    global GRAPH
    # For each key, treat successors as the tokens after the first element
    g = {}
    for k, v in Lines.items():
        if isinstance(v, (list, tuple)):
            succ = tuple(v) if len(v) > 0 else tuple()
        else:
            succ = tuple()
        g[k] = succ
    GRAPH = g
    # clear caches
    try:
        find_out.cache_clear()
    except Exception:
        pass
    try:
        find_out2.cache_clear()
    except Exception:
        pass

@cache
def find_out2(start, end, dac=False, fft=False):
    """Count paths from `start` to `end` that have seen both 'dac' and 'fft'."""
    if not GRAPH:
        return 0
    graph = GRAPH.get(start, ())
    # direct edge to end
    if end in graph:
        return 1 if (dac and fft) else 0

    res = 0
    for node in graph:
        ndac = dac or (node == "dac")
        nfft = fft or (node == "fft")
        res += find_out2(node, end, ndac, nfft)
    return res

@cache
def find_out(start, end):
    """Count paths from `start` to `end`."""
    graph = GRAPH.get(start, ())
    if end in graph:
        return 1
    res = 0
    for node in graph:
        res += find_out(node, end)
    return res

if __name__ == '__main__':
    main(test=True)
    main()
    main(test=True, pt2=True)
    main(pt2=True)

