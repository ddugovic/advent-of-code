"""
--- Day 3: Binary Diagnostic ---
https://adventofcode.com/2021/day/3
"""
from aocd import data

def mode(lines):
    """Determine mode of lines"""
    count = []
    for line in lines:
        for i, bit in enumerate(line):
            if i >= len(count):
                count.append(0)
            if bit == '0':
                count[i] -= 1
            else:
                count[i] += 1
    mode = []
    for i, bit in enumerate(count):
        if i >= len(mode):
            mode.append(0)
        if count[i] >= 0:
            mode[i] = 1
    return mode

def decimal(count):
    """Convert binary string to decimal"""
    return int(count, 2)

def solve():
    """Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them together. What is the power consumption of the submarine?

    Use the binary numbers in your diagnostic report to calculate the oxygen generator rating and CO2 scrubber rating, then multiply them together. What is the life support rating of the submarine?"""

    modes = mode(data.splitlines())
    modestr = ''.join([str(digit) for digit in modes])
    nonmodestr = ''.join([str(1-digit) for digit in modes])
    print("part a:", decimal(modestr) * decimal(nonmodestr))

    prefix = ''
    carbon = ''
    lines = data.splitlines()
    while len(lines) > 1:
        prefix += str(1 - mode(lines)[len(prefix)])
        lines = [line for line in lines if line.startswith(prefix)]
        carbon = lines[0]

    prefix = ''
    oxygen = ''
    lines = data.splitlines()
    while len(lines) > 1:
        prefix += str(mode(lines)[len(prefix)])
        lines = [line for line in lines if line.startswith(prefix)]
        oxygen = lines[0]

    print("part b:", decimal(carbon) * decimal(oxygen))

if __name__ == "__main__":
    solve()
