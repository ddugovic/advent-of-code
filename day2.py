"""Solve https://adventofcode.com/2021/day/2"""
from aocd.models import Puzzle

def main():
    """Solve https://adventofcode.com/2021/day/2"""
    puzzle = Puzzle(year=2021, day=2)

    distance = 0
    depth = 0
    for line in puzzle.input_data.splitlines():
        command = line.split()
        if command[0] == "forward":
            distance += int(command[1])
        elif command[0] == "down":
            depth += int(command[1])
        elif command[0] == "up":
            depth -= int(command[1])
    print (distance * depth)

    aim = 0
    distance = 0
    depth = 0
    for line in puzzle.input_data.splitlines():
        command = line.split()
        if command[0] == "forward":
            distance += int(command[1])
            depth += aim * int(command[1])
        elif command[0] == "down":
            aim += int(command[1])
        elif command[0] == "up":
            aim -= int(command[1])
    print (distance * depth)

if __name__ == "__main__":
    main()
