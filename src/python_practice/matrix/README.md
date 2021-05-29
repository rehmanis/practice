# Problem Statement

You are given a `m x n` matrix with `1s` and `0s`. Update the state of each cell based on the following criteria
If a cell has 3 neighbors with `ON` state set this cell's state to `ON` (i.e set the value to 1). If a cell has 2 neighbors then keep the cell the same value as it is. Otherwise update the state to `OFF` i.e `0`. A neighbor can be in any of the eight directions (i.e diagonal direction is included). An update for all cells should occur simultaneously/atomically.
