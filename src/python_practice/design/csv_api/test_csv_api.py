import os

import pytest
from csv_api import CsvApi


HERE = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture(scope="class")
def csv_handle(filename):
    csv = CsvApi(os.path.join(HERE, "testdata", filename))
    yield csv
    print("\nleaving csv fixture")


@pytest.mark.parametrize(
    "filename,expected",
    [
        (
            "simple_csv.txt",
            [
                ["location", "employee", "favorite fruit", "details", "favorite movie"],
                ["Austin", "Alice", "Apple", "likes red apples", "Batman"],
                ["Boston", "Bob", "Bosc Pear", "likes yellow pears", "Batman"],
            ],
        ),
        (
            "escaped_csv.txt",
            [
                ["location", "employee", "favorite fruit", "details", "favorite movie"],
                [
                    "Washing,ton,DC",
                    "Walter",
                    "Watermelons",
                    "like,square,watermelons",
                    "Waterworld",
                ],
                ["vancouver", "Henry", "tomato", "like red,big tomato", "hello,word"],
            ],
        ),
    ],
    scope="class",
)
class TestCsvApi:
    """test csv file with no escaped commas in the words."""

    def test_csv_api_repr(self, csv_handle, expected):
        assert str(csv_handle) == str(expected)

    def test_csv_get_value_at_valid_position(self, csv_handle, expected):
        result = csv_handle.get_value(2, 3)

        assert result == expected[2][3]

    def test_csv_get_value_at_invalid_position(self, csv_handle, expected):
        with pytest.raises(IndexError):
            csv_handle.get_value(len(expected), len(expected[0]) - 1)

        with pytest.raises(IndexError):
            csv_handle.get_value(len(expected) - 1, len(expected[0]))

        with pytest.raises(IndexError):
            csv_handle.get_value(-1, len(expected[0]) - 1)

        with pytest.raises(IndexError):
            csv_handle.get_value(len(expected) - 1, -1)

    def test_csv_get_row_at_valid_position(self, csv_handle, expected):
        result = csv_handle.get_row(1)

        assert result == expected[1]

    def test_csv_get_row_at_invalid_position(self, csv_handle, expected):
        with pytest.raises(IndexError):
            csv_handle.get_row(len(expected))
        with pytest.raises(IndexError):
            csv_handle.get_row(-1)

    def test_csv_get_col_at_valid_position(self, csv_handle, expected):
        result = csv_handle.get_col(3)
        expected_col = []
        for row in expected:
            expected_col.append(row[3])

        assert result == expected_col

    def test_csv_get_col_at_invalid_position(self, csv_handle, expected):
        with pytest.raises(IndexError):
            csv_handle.get_col(len(expected[0]))
        with pytest.raises(IndexError):
            csv_handle.get_col(-1)

    def test_get_csv_num_rows(self, csv_handle, expected):
        result = csv_handle.get_num_rows()

        assert result == len(expected)

    def test_get_csv_num_cols(self, csv_handle, expected):
        result = csv_handle.get_num_cols()

        assert result == len(expected[0])

    def test_get_csv_headers(self, csv_handle, expected):
        result = csv_handle.get_csv_headers()

        assert result == expected[0]


@pytest.mark.parametrize("filename", [("empty_csv.txt")], scope="class")
class TestCsvApiOnEmptyFile:
    def test_get_csv_num_rows(self, csv_handle):
        result = csv_handle.get_num_rows()

        assert result == 0

    def test_get_csv_num_cols(self, csv_handle):
        result = csv_handle.get_num_cols()

        assert result == 0

    def test_get_csv_headers(self, csv_handle):
        result = csv_handle.get_csv_headers()

        assert result == []
