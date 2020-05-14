import os
import re

def part1():
    pass

def part2():
    pass


def manhattan_dist(p1, p2):
    dist = 0
    for i in range(len(p1)):
        dist += abs(p1[i] - p2[i])
    return dist

def next_bend(p, instruction):
    dir, dist = re.match('([LRUD])([0-9]+)', instruction).groups()
    dist = int(dist)

    if dir == 'L':
        p[0] -= dist
    elif dir == 'R':
        p[0] += dist
    elif dir == 'D':
        p[1] -= dist
    elif dir == 'U':
        p[1] += dist
    else:
        raise(ValueError("Unknown direction: {}".format(dir)))
    
    return p

def find_bends(p, instructions):
    bends = [tuple(p.copy())]
    for instruction in instructions:
        p = next_bend(p, instruction)
        bends.append(tuple(p.copy()))
    return bends



if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        wires = [line.split(',') for line in f.readlines()]

    test_vals = ['R75,D30,R83,U83,L12,D49,R71,U7,L72', 'U62,R66,U55,R34,D71,R55,D58,R83']
    test_ans = 159