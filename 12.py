from file_reader import read_data
import AoC2024.util_for_12 as u

def count_total_borders(matrix):
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    def is_valid(r, c, value):
        return 0 <= r < rows and 0 <= c < cols and matrix[r][c] == value

    def flood_fill(r, c):
        stack = [(r, c)]
        area = []
        while stack:
            x, y = stack.pop()
            if visited[x][y]:
                continue
            visited[x][y] = True
            area.append((x,y))

            for dr, dc in directions:
                nx, ny = x + dr, y + dc
                if is_valid(nx, ny, matrix[r][c]):
                    if not visited[nx][ny]:
                        stack.append((nx, ny))
                    continue
        return area

    # Traverse the matrix and flood-fill each area
    regions = []
    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                region = u.Region(flood_fill(r,c))
                regions.append(region)
    part1_result = 0
    part2_result = 0
    for region in regions:
        #print(region.fences, region.sides)
        part1_result += region.part1
        part2_result += region.part2
        #for line in region.grid:
            #print(line)
        #input()


    return part1_result, part2_result


# Example Usage
matrix = ['RRRRIICCFF',
    'RRRRIICCCF',
    'VVRRRCCFFF',
    'VVRCCCJFFF',
    'VVVVCJJCFE',
    'VVIVCCJJEE',
    'VVIIICJJEE',
    'MIIIIIJJEE',
    'MIIISIJEEE',
    'MMMISSJEEE',
]

matrix = read_data('12.txt')

print(count_total_borders(matrix))
