class Region:
    def __init__(self, all_beds):
        self.beds = all_beds
        self.min_row = min([r for r, _ in all_beds])
        self.max_row = max([r for r, _ in all_beds])
        self.min_col = min([c for _, c in all_beds])
        self.max_col = max([c for _, c in all_beds])
        self.grid = self.construct_grid(self.beds)
        
        self.total_bed_count = len(self.beds)
        self.fences, self.sides = self.estimate()
        self.part1 = self.total_bed_count * self.fences
        self.part2 = self.total_bed_count * self.sides

    def add_bed(self, r, c):
        self.beds.append((r, c))
        self.min_row = min(r, self.min_row)
        self.max_row = max(r, self.max_row)
        self.min_col = min(c, self.min_col)
        self.max_col = max(c, self.max_col)

    def construct_grid(self, beds):
        rows = self.max_row - self.min_row + 1
        cols = self.max_col - self.min_col + 1
        grid = [[False] * cols for _ in range(rows)]  # Proper grid initialization

        for r, c in self.beds:
            grid[r - self.min_row][c - self.min_col] = True  # Correct indexing

        return grid

    def rotate_grid(self, grid):
        # Rotate grid 90 degrees counterclockwise
        return [list(reversed(col)) for col in zip(*grid)]

    def count_borders_one_direction(self, grid):
        count = 0
        sides = []
        # Check top borde

        # Check vertical borders (each row's transition from False to True)
        for gr in range(len(grid)):
            for gc in range(len(grid[0])):
                a = False if gr == 0 else grid[gr-1][gc]
                pattern = (a, grid[gr][gc])
                if pattern == (False, True):
                    count += 1
                else:
                    if count > 0:
                        sides.append(count)
                    count = 0
            if count > 0:
                sides.append(count)
            count = 0
        return sum(sides), len(sides)
    
    def estimate(self):
        fences = 0
        sides = 0
        for _ in range(4):
            self.grid = self.rotate_grid(self.grid)
            f, s = self.count_borders_one_direction(self.grid)
            fences += f
            sides += s
        return fences, sides


