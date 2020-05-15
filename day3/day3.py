import os
import re

def part1(wires):
    # lay out wires and note all points covered on grid
    start_point = [0, 0]
    points_visited = [[], []]
    for idx, wire in enumerate(wires):
        points_visited[idx] = [start_point]
        for instruction in wire:
            next_segment = get_next_segment(points_visited[idx][-1], instruction)
            points_visited[idx].extend(next_segment)
        points_visited[idx] = [tuple(pt) for pt in points_visited[idx]]

    # get common points in lists
    common_points = get_common_points(start_point, *points_visited)

    # get nearest point
    min_dist = 1e9
    for pt in common_points:
        new_dist = manhattan_dist(start_point, pt)
        min_dist = new_dist if new_dist < min_dist else min_dist
    
    return min_dist

def part2():
    pass


def manhattan_dist(p1, p2):
    dist = 0
    for i in range(len(p1)):
        dist += abs(p1[i] - p2[i])
    return dist

def parse_instruction(instruction):
    # extract info
    dir, dist = re.match('([LRUD])([0-9]+)', instruction).groups()
    dist = int(dist)

    # determine which index changes and by how much
    idx = 0 if dir in ['L', 'R'] else 1
    sign = 1 if dir in ['R', 'U'] else -1

    return idx, dist, sign

def get_next_segment(start_point, instruction):
    idx_travel, dist, sign = parse_instruction(instruction)
    idx_const = 0 if idx_travel else 1

    segment = []
    for step in range(1*sign, (dist+1)*sign, sign):
        next_point = [None, None]
        next_point[idx_const] = start_point[idx_const]
        next_point[idx_travel] = start_point[idx_travel] + step
        segment.append(next_point)

    return segment

def follow_path(start_point, instructions):
    visited_points = []
    return visited_points


def get_common_points(start_pt, pts1, pts2):
    return list(set.intersection(set(pts1), set(pts2).symmetric_difference({(0,0)})))


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        wires = [line.split(',') for line in f.readlines()]

    a = part1(wires)
    print("Part 1: {}".format(a))