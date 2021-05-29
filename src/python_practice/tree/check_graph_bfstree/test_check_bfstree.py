import pytest
from check_bfstree import is_graph_bfstree_inplace


@pytest.mark.parametrize(
    "graph,expected,root",
    [
        ([[2], [2], [0, 1]], False, 2),
        ([[1], [0, 2], [1]], True, 1),
        ([[1], [0, 3, 2], [1], [1]], False, 1),
        ([[]], True, 0),
        ([[2], [3], [5, 0], [1, 4], [3, 5], [4, 6, 2], [5]], False, 4),
        ([[1], [0, 2], [1, 4], [4], [2, 5, 3], [4]], True, 0),
        ([[1], [0, 2], [1, 4], [4], [2, 5, 3], [4]], True, 1),
        ([[1], [0, 2], [1, 4], [4], [2, 5, 3], [4]], True, 2),
        ([[1], [0, 2], [1, 4], [4], [2, 5, 3], [4]], False, 3),
        ([[1], [0, 2], [1, 4], [4], [2, 5, 3], [4]], False, 4),
        ([[1], [0, 2], [1, 4], [4], [2, 5, 3], [4]], False, 5),
        ([[1], [0, 3], [4], [1, 4], [5, 2, 3], [4]], False, 1),
        ([[1], [0, 3], [4], [1, 4], [5, 2, 3], [4]], False, 1),
    ],
)
def test_is_bfstree_private(graph, root, expected):
    result = is_graph_bfstree_inplace(graph, root)

    assert result == expected
