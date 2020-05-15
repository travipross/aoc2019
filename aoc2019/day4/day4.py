import math


def extract_digits(n):
    return [ int(d) for d in str(n) ]

def only_ascends(digits):
    return all([ digits[i] >= digits[i-1] for i in range(1, len(digits))])

def has_repeating_digits(digits, max_2=False):
    repeated = 1
    prev_digit = None
    for d in digits:
        # increment sequential match count if same as previous
        if d == prev_digit:
            repeated += 1
        # return true if sequence quota was met
        elif repeated == 2:
            return True
        else:
            repeated = 1
        prev_digit = d

        # if not limiting sequence quota, quit as soon as sequence was found
        if not max_2 and repeated >= 2:
            return True

    # if final sequence was 2        
    return repeated == 2

def password_is_valid(n, num_digits=6, max_2=False):
    digits = extract_digits(n)
    return only_ascends(digits) and has_repeating_digits(digits, max_2) and len(digits) == num_digits

def part1(n_min, n_max):
    return sum([ password_is_valid(n) for n in range(n_min, n_max)])

def part2(n_min, n_max):
    return sum([ password_is_valid(n, max_2=True) for n in range(n_min, n_max)])


if __name__ == "__main__":
    puzzle_input = [240298, 784956]

    a = part1(*puzzle_input)
    print("Part 1: {}".format(a))

    b = part2(*puzzle_input)
    print("Part 2: {}".format(b))
