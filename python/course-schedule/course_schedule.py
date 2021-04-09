import sys
from typing import List


class Solution:

    def compute_adj_list(self, edges: List[int], nodes):
        adj = {}

        for node in range(nodes):
            adj[node] = []

        for edge in edges:
            adj[edge[0]].append(edge[1])

        return adj

    def has_cycle(self, adj, v, visited, onstack):
        visited[v] = True
        onstack[v] = True

        for neighbor in adj[v]:

            if (
                not visited[neighbor] and
                self.has_cycle(adj, neighbor, visited, onstack)
            ):
                return True
            elif onstack[neighbor]:
                return True

        onstack[v] = False

        return False

    def can_finish(
        self, numCourses: int, prerequisites: List[List[int]]
    ) -> bool:

        adj = self.compute_adj_list(prerequisites, numCourses)
        visited = [False] * numCourses
        onstack = [False] * numCourses

        for course in range(numCourses):

            is_cycle = self.has_cycle(adj, course, visited, onstack)

            if is_cycle:
                return False

        return True


def main(argv, argc):
    sol = Solution()
    numCourses = 2
    edges = [[0, 1], [1, 0]]
    print(sol.can_finish(numCourses, edges))


if __name__ == "__main__":
    main(sys.argv, len(sys.argv))
