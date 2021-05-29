from typing import List


def is_graph_bfstree_recursive(graph: List[List[int]], root: int) -> bool:
    """given a acyclic complete graph, returns whether it is a binary search tree
    or not.

    Note: bst is one where the parent nodes key is greater then all
    of the keys in its left subtree and less than all key in its right subtree


    Strategy is to store the current min and max values. The current node must be
    within this range for it to be bstree. We start with min -inf and max inf. For
    the right neighbor i.e node less than current root we recursively call the
    function but with root as the right node and min value as the current root value
    as we know that all values in the right subtree must be greater than this current
    root i.e. this new min value (we keep the max the same as before). For left
    subtree we recursively call function on left node as root, and max value to be
    current root. Parent is also passed during recursion to make sure not to visit
    it again

    :param graph: an adjacency list where index is the node number and list at
                  that index is its neighbors
    :type graph: List[List[int]]
    :param root: the root from which to check if the graph is bst
    :type root: int
    :return: True if graph is bst for the given root, False otherwise
    :rtype: bool
    """

    return _is_graph_bfstree(graph, root, -1, float("-inf"), float("inf"))


def _is_graph_bfstree(
    graph: List[List[int]], root: int, parent: int, min_val: int, max_val: int
) -> bool:
    """Helper function for finding if the given graph is BST

    :param graph: an adjacency list where index is the node number and list at
                  that index is its neighbors
    :type graph: List[List[int]]
    :param root: the root from which to check if the graph is bst
    :type root: int
    :param parent: the parent of current root, None if no parent
    :type parent: int
    :param min_val: the current min value that a given node must be greater than for
                    graph to be BST
    :type min_val: int
    :param max_val: the current max value that a given node must be less than for graph
                    to be BST
    :type max_val: int
    :return: True if graph is bst for the given root, False otherwise
    :rtype: bool
    """

    if root <= min_val or root >= max_val:
        return False

    selected_left = False
    selected_right = False
    left = True
    right = True

    for nei in graph[root]:

        if nei == parent:
            continue

        if selected_left and nei < root:
            return False

        if selected_right and nei > root:
            return False

        if nei < root:
            selected_left = True
            left = _is_graph_bfstree(graph, nei, root, min_val, root)
        else:
            selected_right = True
            right = _is_graph_bfstree(graph, nei, root, root, max_val)

    return left and right
