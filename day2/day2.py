import os

def part1(vals):
    vals[1] = 12
    vals[2] = 2
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

if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
        vals = list(map(int, f.read().split(',')))
    
    a = part1(vals)
    print("Part 1 answer: {}".format(a))