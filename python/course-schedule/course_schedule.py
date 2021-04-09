import sys
import os
from typing import List
from typing import Dict

FILE_PATH = os.path.abspath(__file__)


class Solution:
    """Solution class for whether all course can be finished given their
    prerequisites all courses
    """

    def compute_adj_list(
        self, edges: List[int], numNodes: int
    ) -> Dict[int, List[int]]:
        """Compute adjacency list(graph) from given number of nodes and edges

        :param edges: a list of directed edges
        :type edges: List[int]
        :param numNodes: total number of nodes in the graph to be constructed
        :type numNodes: int
        :return: adjacency list graph
        :rtype: Dict[int, List[int]]
        """
        adj = {}

        for node in range(numNodes):
            adj[node] = []

        for edge in edges:
            adj[edge[0]].append(edge[1])

        return adj

    def has_cycle(
        self,
        adj: Dict[int, List[int]],
        v: int,
        visited: List[bool],
        onstack: List[bool]
    ) -> bool:
        """Computes whether a directed graph as a cycle

        :param adj: an adjacency list
        :type adj: Dict[int, List[int]]
        :param v: the node from which to perform dfs to detect cycles
        :type v: int
        :param visited: keep track of whether a node has been visited or not
        :type visited: List[bool]
        :param onstack: keep track of whether a node is in the recursion stack
                        trace or not
        :type onstack: List[bool]
        :return: True if cycle is found in directed graph false otherwise
        :rtype: bool
        """
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
        """Finds whether all course can be completed given a list
        of prerequisites

        :param numCourses: The total number of courses to be completed
        :type numCourses: int
        :param prerequisites: a list of prerequisites. Example if we have
                              [[0, 1], [0, 2]], course 0 must be completed
                              before either course 1 or 2, can be taken
        :type prerequisites: List[List[int]]
        :return: true if all courses can be completed given the prerequisites
                 or false otherwise
        :rtype: bool
        """

        adj = self.compute_adj_list(prerequisites, numCourses)
        visited = [False] * numCourses
        onstack = [False] * numCourses

        for course in range(numCourses):

            is_cycle = self.has_cycle(adj, course, visited, onstack)

            if is_cycle:
                return False

        return True
