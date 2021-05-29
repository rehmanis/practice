import pytest
from update_state import update_state


@pytest.mark.parametrize(
    "input,expected",
    [
        (
            [[1, 0, 0, 0, 1], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0], [0, 1, 1, 0, 0]],
            [[0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0], [0, 1, 1, 0, 0]],
        ),
        (
            [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]],
            [[1, 0, 0, 1], [0, 0, 0, 0], [1, 0, 0, 1]],
        ),
        (
            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
        ),
    ],
)
def test_is_bfstree_private(input, expected):
    result = update_state(input)

    assert result == expected
