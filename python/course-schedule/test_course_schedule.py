import pytest
from course_schedule import Solution


@pytest.mark.parametrize(
    "nodes,edges,expected", [
        (2, [[0, 1], [1, 0]], False),
        (2, [[0, 1]], True),
        (6, [[1, 4], [2, 4], [3, 1], [3, 2]], True),
        (
            10,
            [[5, 7], [1, 2], [2, 3], [1, 3], [3, 4], [1, 4], [2, 5], [3, 5]],
            True
        )
    ]
)
def test_can_finish(nodes, edges, expected):
    sol = Solution()
    result = sol.can_finish(nodes, edges)

    assert result is expected
