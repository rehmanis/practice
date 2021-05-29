import copy
from typing import List


def update_state(grid: List[List[int]]) -> List[List[int]]:
    """update the state of all cell simultaneously based on the following criteria:

    If a cell has 3 neighbors with `ON` state set this cell's state to `ON` (i.e set
    the value to 1). If a cell has 2 neighbors then keep the cell the same value as it
    is. Otherwise update the state to `OFF` i.e `0`. A cell can have at most 8 neighbors

    :param grid: m x n matrix of ON/OFF states
    :type grid: List[List[int]]
    :return: m x n matrix with updated states
    :rtype: List[List[int]]
    """

    next_states = copy.deepcopy(grid)

    for row in range(len(grid)):
        for col in range(len(grid[0])):

            count = get_count(grid, row, col)

            if count == 3:
                next_states[row][col] = 1
            elif count != 2:
                next_states[row][col] = 0

    return next_states


def get_count(grid: List[List[int]], row: int, col: int) -> int:
    """find the number of ON states for at most 8 neighbors of given grid position

    :param grid: m x n matrix of ON/OFF states
    :type grid: List[List[int]]
    :param row: the row position of cell for which we want to find the number of
                neighbors with ON states
    :type row: int
    :param col: the col position of cell for which we want to find the number of
                neighbors with ON states
    :type col: int
    :return: total number of ON state neighbors for given cell position (row, col)
    :rtype: int
    """

    # up, down, left right, top, top left, top right, bottom right, bottom left
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, 1), (1, -1)]
    count = 0

    for direction in directions:
        next_row = row + direction[0]
        next_col = col + direction[1]

        if not _is_out_of_bounds(next_row, next_col, len(grid), len(grid[0])):
            count += grid[next_row][next_col]

    return count


def _is_out_of_bounds(row: int, col: int, rows: int, cols: int) -> bool:
    """helper method to determine if given row, col are out of bounds

    :param row: row position
    :type row: int
    :param col: col position
    :type col: int
    :param rows: total number of rows
    :type rows: int
    :param cols: total number of cols
    :type cols: int
    :return: True if row, col is outside the specified row and col size, False
             otherwise
    :rtype: bool
    """

    if row < 0 or col < 0 or row >= rows or col >= cols:
        return True

    return False
