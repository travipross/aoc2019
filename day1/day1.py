def divide_round_subtract(num, divisor=3, difference=2, recursive=False):
    if not recursive:
        return int(num/divisor)-difference
    else:
        amt = int(num/divisor)-difference
        if amt <= 0:
            return 0
        else:
            return amt + divide_round_subtract(amt, divisor=divisor, difference=difference, recursive=recursive)

def part1(input_vals):
    return sum(map(divide_round_subtract, input_vals))

def part2(input_vals):
    return sum(map(lambda x: divide_round_subtract(x, recursive=True), input_vals)) 

if __name__ == "__main__":
    with open("input.txt") as f:
        vals = list(map(int, f.readlines()))

    a = part1(vals)
    print("Answer for part 1: {}".format(a))

    b = part2(vals)
    print("Answer for part 2: {}".format(b))
