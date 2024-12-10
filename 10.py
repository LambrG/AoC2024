from file_reader import read_data
from collections import deque

dataset = read_data('10.txt')
testset = read_data('test.txt')
lava_map = [[int(x) for x in line ] for line in dataset]

DIRECTIONS = [
    (-1,  0),
    ( 0,  1),
    ( 1,  0),
    ( 0, -1)
]

steps = deque()
trailheads = []
result = 0

for r in range(len(lava_map)):
    for c in range(len(lava_map[r])):
        if lava_map[r][c] == 0:
            trailheads.append((r,c))

for r,c in trailheads:
    steps = deque()
    steps.append((r,c))
    for searched_value in range(1,10):
        for i in range(len(steps)):
            nr, nc = steps.popleft()
            for dr, dc in DIRECTIONS:
                sr = nr+dr
                sc = nc+dc
                if sr < 0 or sr >= len(lava_map) or sc < 0 or sc >= len(lava_map[0]):
                    continue
                else:
                    if lava_map[sr][sc] == searched_value:
                        """if (sr, sc) in steps:
                            continue
                        else: """
                        steps.append((nr+dr, nc+dc))
    result += len(steps)

print(result)    
