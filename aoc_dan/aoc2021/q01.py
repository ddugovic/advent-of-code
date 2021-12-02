"""
--- Day 1: Sonar Sweep ---
https://adventofcode.com/2021/day/1
"""
from aocd import data

def solve():
    """How many measurements are larger than the previous measurement?
    Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?"""

    count1 = 0
    count2 = 0
    lastdepth = 0
    lastsum = 0
    window = [0, 0, 0]
    for step, depth in enumerate(data.splitlines()):
        depth = int(depth)
        if step >= 1 and depth > lastdepth:
            count1 = count1 + 1
        lastdepth = depth

        window = window[1:]
        window.append(depth)
        if step >= 3 and sum(window) > lastsum:
            count2 = count2 + 1
        lastsum = sum(window)

    print("part a:", count1)
    print("part b:", count2)

if __name__ == "__main__":
    solve()
