from typing import List
from typing import Set
from typing import Tuple


class Solution:
    def pacific_atlantic(self, heights: List[List[int]]) -> Set[Tuple[int, int]]:
        """finds the set of locations(row, col) in a grid heights from which
        water can flow to both the pacific and Atlantic oceans. Water in each
        cell can only follow either up, down, left or right and can only flow
        from a cell to an adjacent one with an equal or lower height.

        Example `heights` values

                pacific ocean
                __ __ __ __ __

        pacifc | 1  2  2  3  5 | atlantic
        ocean  | 3  2  3  4  4 | ocean
               | 2  4  5  3  1 |
               | 6  7  1  4  5 |
                __ __ __ __ __
                pacific ocean

        :param heights: representing the height of each unit cell in a
                        continent
        :type heights: List[List[int]]
        :return: set of grid coordinates where water can flow to both the
                 Pacific and Atlantic oceans.
        :rtype: Set[Tuple[int, int]]
        """

        rows = len(heights)
        cols = len(heights[0])
        visited_pacific = set()
        visited_atlantic = set()

        # find all nodes visited starting from only those nodes adjacent to
        # pacific ocean (i.e (row, 0) or (0, cols)). Only visit adjacent nodes
        # in dfs if the height of current is smaller than the adjacent node.
        # Repeat this for atlantic and then find the intersection of the
        # two visited sets for both oceans to find the solution
        # Complexity O(m . n)
        for row in range(rows):

            self.dfs(heights, (row, 0), visited_pacific, -1)
            self.dfs(heights, (row, cols - 1), visited_atlantic, -1)

        for col in range(cols):

            self.dfs(heights, (0, col), visited_pacific, -1)
            self.dfs(heights, (rows - 1, col), visited_atlantic, -1)

        return visited_pacific & visited_atlantic

    def dfs(
        self,
        heights: List[List[int]],
        start: Tuple[int, int],
        visited: Set,
        val: int,
    ):
        """performs a depth first search(dfs) starting from grid location `start'

        :param heights: representing the height of each unit cell in a
                        continent
        :type heights: List[List[int]]
        :param start: the grid location (row, col) which is the start of dfs
        :type start: Tuple[int, int]
        :param visited: a set of all grid locations that have been visited so
                        far while performing dfs
        :type visited: Set
        :param val: the height of parent/last visited node in the dfs
        :type val: int
        """
        row, col = start

        # if row or col is out of bounds, or if the height of previous
        # locations is greater than current one, terminate dfs
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

        # perform dfs on adjacent cells in all 4 directions
        self.dfs(heights, (row + 1, col), visited, heights[row][col])
        self.dfs(heights, (row, col + 1), visited, heights[row][col])
        self.dfs(heights, (row - 1, col), visited, heights[row][col])
        self.dfs(heights, (row, col - 1), visited, heights[row][col])
