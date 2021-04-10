import pytest
from sum_of_two_integers import Solution


@pytest.mark.parametrize(
    "a, b, bits, expected",
    [
        (-1, 1, 11, 0),  # add same -ve and +ve values
        (-16, 15, 5, -1),  # add -ve > +ve and TMIN + TMAX for given bit size
        (10, 15, 11, 25),  # add both positive
        (1023, -23, 11, 1000),  # add -ve < +ve
        (0, 0, 11, 0),  # add zeros
        (4294967295, -2147483641, 33, 2147483654),  # add big numbers
    ],
)
def test_get_sum_without_plus_minus_ops_valid_input(a, b, bits, expected):
    sol = Solution(bits)
    result = sol.get_sum(a, b)

    assert result == expected


@pytest.mark.parametrize(
    "a, b, bits", [(-100, 1, 7), (-16, 16, 5), (15, 128, 8)]
)
def test_get_sum_without_plus_minus_ops_invalid_inputs(a, b, bits):
    sol = Solution(bits)
    with pytest.raises(SystemExit):
        sol.get_sum(a, b)
