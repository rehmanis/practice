import os
from typing import List

HERE = os.path.dirname(os.path.abspath(__file__))


class CsvApi:
    def __init__(self, filename: str):
        self.data = []
        self._read_file(filename)

    def __repr__(self) -> str:
        return str(self.data)

    def _read_file(self, filename: str) -> None:
        """helper method to read the csv file and store the content
        in a data structure for convenient access

        :param filename: path to the csv file
        :type filename: str
        """

        with open(filename) as csv_file:

            for line in csv_file:

                left_idx = 0
                curr_str = ""
                csv_row = []

                for i in range(1, len(line)):

                    if line[i - 1] == "\\" and line[i] == ",":
                        curr_str += line[left_idx : i - 1]
                        left_idx = i

                    elif line[i - 1] != "\\" and line[i] == "," or line[i] == "\n":
                        curr_str += line[left_idx:i]
                        csv_row.append(curr_str)
                        left_idx = i + 1
                        curr_str = ""

                self.data.append(csv_row)

    def get_value(self, row: int, col: int) -> str:
        """get the value at given row, col for the stored csv file

        :param row: the row number (indexed from 0) of the desired csv content
        :type row: int
        :param col: the col number (indexed from 0) of the desired csv content
        :type col: int
        :raises IndexError: if row or col is negative or geq total number of rows or
                            columns
        :return: the value at the specified row, col
        :rtype: str
        """

        if row < 0 or col < 0 or row >= len(self.data) or col > len(self.data[0]):
            raise IndexError("Inavlid row and/or col")

        return self.data[row][col]

    def get_row(self, row: int) -> List[str]:
        """retreive a csv row

        :param row: the row number of csv content
        :type row: int
        :raises IndexError: if row is negative or geq total number of rows
        :return: a row of csv content
        :rtype: List[str]
        """

        if row < 0 or row >= len(self.data):
            raise IndexError("Invalid row")

        return self.data[row]

    def get_col(self, col: int) -> List[str]:
        """retreive a csv column

        :param col: the column number of csv content
        :type col: int
        :raises IndexError: IndexError: if col is negative or geq total number of
                            columns
        :return: a column of csv content
        :rtype: List[str]
        """

        if col < 0 or col >= len(self.data[0]):
            raise IndexError("Invalid col")

        res = []

        for row in self.data:
            for i in range(len(row)):
                if i == col:
                    res.append(row[i])
        return res

    def get_num_rows(self) -> int:
        """get the total number of rows in stored csv file

        :return: total number of rows
        :rtype: int
        """
        return len(self.data)

    def get_num_cols(self) -> int:
        """get the total number of columns in stored csv file

        :return: total number of columns
        :rtype: int
        """
        if len(self.data):
            return len(self.data[0])
        return 0

    def get_csv_headers(self) -> List[str]:
        """get the csv content headers

        :return: a list of all csv headers i.e the first row
        :rtype: List[str]
        """
        if len(self.data):
            return self.data[0]
        return []
