# 695. Max Area of Island

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
