from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=1)

count1 = 0
count2 = 0
lastdepth = 0
lastsum = 0
window = [0, 0, 0]
for iter, depth in enumerate(puzzle.input_data.splitlines()):
  depth = int(depth)
  if iter >= 1 and depth > lastdepth:
    count1 = count1 + 1
  lastdepth = depth

  window = window[1:]
  window.append(depth)
  if iter >= 3 and sum(window) > lastsum:
    count2 = count2 + 1
  lastsum = sum(window)

print (count1, count2)
