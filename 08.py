from file_reader import read_data
from collections import defaultdict

def check_for_antinodes(r,c,positions):
    result = set()
    for pr, pc in positions:
        if pr == r and pc == c:
            continue
        else:
            ar = r + r - pr
            ac = c + c - pc
            if ar >= 0 and ar < MAX_R and ac >= 0 and ac < MAX_C:
                result.add((ar,ac))
    return result

def part2(r,c,positions):
    for pr, pc in positions:
       part2_antinodes.add((pr,pc))
       dr = r - pr
       dc = c - pc
       find_resonance(pr,pc,dr,dc)

def find_resonance(r,c,dr,dc):
    new_r = r + dr
    new_c = c + dc
    if new_r < 0 or new_r >= MAX_R or new_c < 0 or new_c >= MAX_R or (dr == 0 and dc == 0):
        return
    else:
        part2_antinodes.add((new_r,new_c))
        find_resonance(new_r,new_c,dr, dc)

dataset = read_data('08.txt')

map_of_antenas = defaultdict(list)

MAX_R = len(dataset)
MAX_C = len(dataset[0])

for r, line in enumerate(dataset):
    for c, char in enumerate(line):
        if char != '.':
            map_of_antenas[char].append((r,c))

antinodes_list = set()
part2_antinodes = set()


for antena_type, positions in map_of_antenas.items():
    for r,c in positions:
        antinodes_list.update(check_for_antinodes(r,c,positions))
        part2(r,c,positions)
             

print(len(antinodes_list))
print(len(part2_antinodes))
""" for i in antinodes_list:
    print(i) """