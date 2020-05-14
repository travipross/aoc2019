import os

def run_program(vals, input_1, input_2):
    vals[1] = input_1
    vals[2] = input_2

    idx = 0
    while idx < len(vals)-4:
        opnum, idx_n1, idx_n2, res_idx = vals[idx:idx+4]
        if opnum == 1:
            vals[res_idx] = vals[idx_n1] + vals[idx_n2]
        elif opnum == 2:
            vals[res_idx] = vals[idx_n1] * vals[idx_n2]
        elif opnum == 99:
            break
        else:
            print("ERROR: Unexpected operation: {}".format(opnum))
        idx += 4
    
    return vals[0]

def part1(vals):
    return run_program(vals, 12, 2)

def part2(vals, target):
    for i in range(100):
        for j in range(100):
            res = run_program(vals.copy(), i, j)

            if res == target:
                return 100 * i + j


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        vals = list(map(int, f.read().split(',')))
    
    a = part1(vals.copy())
    print("Part 1 answer: {}".format(a))

    b = part2(vals.copy(), 19690720)
    print("Part 2 answer: {}".format(b))