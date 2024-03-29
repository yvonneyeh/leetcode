# 695. Max Area of Island

class Solution:

    def dfs(self, grid, r, c):
        grid[r][c] = 0
        num = 1
        lst = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
        for row, col in lst:
            if row >= 0 and col >= 0 and row < len(grid) and col < len(grid[row]) and grid[row][col] == 1:
                num += self.dfs(grid, row, col)
        return num

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area_islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    area_islands = max(area_islands, self.dfs(grid, r, c))
        return area_islands

# Runtime: 140 ms, faster than 65.13% of Python3 online submissions for Max Area of Island.
# Memory Usage: 17.3 MB, less than 23.66% of Python3 online submissions for Max Area of Island.

# def dfs(map, r, c):
#         # What if we can’t mutate map?
#         map[r][c] = 'x'
#         num = 1
#         lst = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
#         for row, column in lst:
#             if row >= 0 and column >= 0 and row < len(map) and column < len(map[row]) and map[row][column] == 'o':
#                 num += dfs(map, row, column)
#         return num
#
# def getSizeOfLargestIsland(map):
#         island_area = 0
#         for r in range(len(map)):
# 	# Is there a guarantee that the map is a square?
#             for c in range(len(map[r])):
#                 if map[r][c] == 'o':
#                     island_area = max(island_area, dfs(map, r, c))
#         return island_area


class Solution:

    def dfs(self, grid, r, c):
        grid[r][c] = 0
        num = 1
        lst = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
        for row, col in lst:
            if row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0]) and grid[row][col] == 1:
                num += self.dfs(grid, row, col)
        return num

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area_islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    area_islands = max(area_islands, self.dfs(grid, r, c))
        return area_islands


# Depth First Search:

class SolutionDFS:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0

        def helper(row, col):
            nonlocal max_area, area
			# Base case, we ensure that we are at a valid location; in the grid and on an island.
            if row >= rows or row < 0 or col >= cols or  col < 0 or grid[row][col] != 1:
                return
			# Update area and mark the location so it doesn't ge recounted.
            area = area + 1
            grid[row][col] = '#'
			# Continue searching in adjacent locations.
            helper(row + 1, col)
            helper(row - 1, col)
            helper(row, col + 1)
            helper(row, col - 1)

		# Search for islands.
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
				    # If we find an island use our helper to get it's area and check if it's the largest we've seen.
                    area = 0
                    helper(row, col)
                    max_area = max(area, max_area)
        return max_area

# Breadth First Search:

class SolutionBFS:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        max_area = 0
        # Search our grid looking for islands.
        for row in range(rows):
            for col in range(cols):
			# If we find and island, continue searching it.
                if grid[row][col] == 1:
                    area = 1
					# Mark the locations we've searched so we don't recount them.
                    grid[row][col] = '#'
                    q = collections.deque([])
                    q.append((row, col))
                    while q:
                        r, c = q.popleft()
						# Search all of the possible next locations based on our move directions.
                        for y, x in directions:
						    # new row and col = current + the new movement direction.
                            nr = r + y
                            nc = c + x
							# If the new location is valid: within the grid and contains more island (1)
                            if nr < rows and nr >= 0 and nc < cols and nc >= 0 and grid[nr][nc] == 1:
							    # Update the current islands area, mark as searched and add to the deque.
                                area += 1
                                grid[nr][nc] = '#'
                                q.append((nr, nc))
                    # Once we finish exploring the island, check if it's area is the largest we've seen thus far.
                    max_area = max(max_area, area)

        return max_area


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        biggestIslandArea = 0

        for r in range(rows):
            for c in range(cols):
                if (grid[r][c] == 1):  # only if the cell is a land
                    # we have found an island
                    biggestIslandArea = max(
                        biggestIslandArea, self.visitIslandDFS(grid, r, c))

        return biggestIslandArea


    def visitIslandDFS(self, grid,  x,  y):
        if (x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0])):
            return 0  # return, if it is not a valid cell
        if (grid[x][y] == 0):
            return 0  # return, if it is a water cell

        grid[x][y] = 0  # mark the cell visited by making it a water cell

        area = 1 # counting the current cell
        # recursively visit all neighboring cells (horizontally & vertically)
        area += self.visitIslandDFS(grid, x + 1, y)  # lower cell
        area += self.visitIslandDFS(grid, x - 1, y)  # upper cell
        area += self.visitIslandDFS(grid, x, y + 1)  # right cell
        area += self.visitIslandDFS(grid, x, y - 1)  # left cell
        return area
