from typing import List


class Solution:
    def pacific_atlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows = len(heights)
        cols = len(heights[0])
        visited_pacific = set()
        visited_atlantic = set()

        for row in range(rows):

            self.dfs(heights, (row, 0), visited_pacific, -1)
            self.dfs(heights, (row, cols - 1), visited_atlantic, -1)

        for col in range(cols):

            self.dfs(heights, (0, col), visited_pacific, -1)
            self.dfs(heights, (rows - 1, col), visited_atlantic, -1)

        return visited_pacific & visited_atlantic

    def dfs(self, heights, start, visited, val):
        row, col = start

        if (
            row >= len(heights)
            or col >= len(heights[0])
            or row < 0
            or col < 0
            or (row, col) in visited
            or heights[row][col] < val
        ):
            return

        visited.add(start)

        self.dfs(heights, (row + 1, col), visited, heights[row][col])
        self.dfs(heights, (row, col + 1), visited, heights[row][col])
        self.dfs(heights, (row - 1, col), visited, heights[row][col])
        self.dfs(heights, (row, col - 1), visited, heights[row][col])
