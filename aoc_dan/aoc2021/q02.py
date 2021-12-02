"""
--- Day 2: Dive! ---
https://adventofcode.com/2021/day/2
"""
from aocd import data

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
