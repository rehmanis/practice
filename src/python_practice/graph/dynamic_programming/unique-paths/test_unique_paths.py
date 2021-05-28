import pytest
from unique_paths import Solution


@pytest.mark.parametrize(
    "m, n, expected",
    [(3, 2, 3), (3, 7, 28), (7, 3, 28), (1, 1, 1), (4, 4, 20), (7, 5, 210)],
)
def test_get_num_unique_paths(m, n, expected):
    sol = Solution()
    result = sol.num_unique_paths(m, n)

    assert result == expected
