from file_reader import read_data


dataset = read_data('06.txt')

map_of_area = []

for r, line in enumerate(dataset):
    row = []
    for c, char in enumerate(line):
        if char == "^":
            sr, sc = r, c
        row.append(char)
    map_of_area.append(row)

MAX_R = len(map_of_area)
MAX_C = len(map_of_area[0])



def part1(r,c):
    dr = -1
    dc = 0
    visited_positions = set()
    visited_positions.add((r,c))
    while True:
        visited_positions.add((r,c))
        if r+dr < 0 or r+dr >= MAX_R or c+dc < 0 or c+dc >= MAX_C: break
        if map_of_area[r+dr][c+dc] == "#":
            dr, dc = dc, -dr
        else:
            r += dr
            c += dc
                
    return len(visited_positions)

def part2(mapa, r,c):
    dr = -1
    dc = 0
    visited = set()
    while True:
        visited.add((r,c,dr,dc))
        if r+dr < 0 or r+dr >= MAX_R or c+dc < 0 or c+dc >= MAX_C: return False
        if mapa[r+dr][c+dc] == "#":
            dr, dc = dc, -dr
        else:
            r += dr
            c += dc
        if (r,c,dr,dc) in visited:
            return True




print(part1(sr,sc))
count = 0
for r in range(len(map_of_area)):
    for c in range(len(map_of_area[r])):
        if map_of_area[r][c] == ".":
            map_of_area[r][c] = "#"
            if part2(map_of_area, sr, sc):
                count += 1
            map_of_area[r][c] = "."
        

print(count)