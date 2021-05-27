class Solution:
    def num_unique_paths(self, m: int, n: int) -> int:
        """find unique paths in a (m x n) grid starting from `row = 0` and
        `col = 0`  to `row = m - 1` and `col = n - 1`. A path consist of steps
        either to the right or downwards (no diagonals step allowed)

        :param m: number of rows in the grid
        :type m: int
        :param n: number of cols in the grid
        :type n: int
        :return: number of unique paths from top left corner of the grid to
                 bottom right corner where each step is either to the right or
                 down
        :rtype: int
        """

        # initialise a DP matrix to store the previous results
        grid = [[1 for _ in range(n)] for _ in range(m)]

        for row in range(1, m):
            for col in range(1, n):
                # recurrance relation: f(i, j) = f(i - 1, j) + f(i, j - 1)
                grid[row][col] = grid[row - 1][col] + grid[row][col - 1]

        return grid[-1][-1]
