"""
--- Day 2: Dive! ---
https://adventofcode.com/2021/day/2
"""
from aocd import data

def solve():
    """Calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth?

    Using this new interpretation of the commands, calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth?"""

    distance = 0
    depth = 0
    for line in data.splitlines():
        command = line.split()
        if command[0] == "forward":
            distance += int(command[1])
        elif command[0] == "down":
            depth += int(command[1])
        elif command[0] == "up":
            depth -= int(command[1])
    print("part a:", distance * depth)

    aim = 0
    distance = 0
    depth = 0
    for line in data.splitlines():
        command = line.split()
        if command[0] == "forward":
            distance += int(command[1])
            depth += aim * int(command[1])
        elif command[0] == "down":
            aim += int(command[1])
        elif command[0] == "up":
            aim -= int(command[1])
    print("part b:", distance * depth)

if __name__ == "__main__":
    solve()
