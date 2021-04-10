import sys


class Solution:

    def __init__(self, bit_size: int):
        """initialise the solution class for a given bit size. Example if
        bit_size = 11 the the range of integers supported is [-1024, 1023]

        :param bit_size: the max bit size supported
        :type bit_size: int
        """
        self._bit_size = bit_size
        self._tmin = -2**(bit_size - 1)
        self._tmax = 2**(bit_size - 1) - 1

    def get_sum(self, a: int, b: int) -> int:
        """finds the sum of two number without using '+' or '-' opperators

        :param a: the first operand, a signed number
        :type a: int
        :param b: the second operand, a signed number
        :type b: int
        :return: the sum of a and b
        :rtype: int
        """

        if a > self._tmax or a < self._tmin:
            print(
                f"Error: signed integer '{a}' cannot be supported by "
                f"{self._bit_size} bits"
            )
            sys.exit(1)

        if b > self._tmax or b < self._tmin:
            print(
                f"Error: signed integer '{b}' cannot be supported by "
                f"{self._bit_size} bits"
            )
            sys.exit(1)

        bit_mask = 1
        carry = 0
        result = 0

        # we use XOR to sum each individual bits
        for _ in range(self._bit_size):
            # need MASK to only XOR the current bit
            result |= (a ^ b ^ carry) & bit_mask
            # keep track of carry bit i.e the overflow bit
            carry = (carry & a) | (carry & b) | (a & b) & bit_mask
            # shift one bit left for both carry and mask so that all bits are 0
            # except for the next bit that will be XORed
            carry = carry << 1
            bit_mask = bit_mask << 1

        # In case the result would be negative, we need to append 1s to all
        # leading bits from bit max_bits onwards. We can do this by ORing with
        # the TMIN which is -1024 for max_bits = 11
        if (
            (b < 0 and a < 0) or
            (b < 0 and abs(b) > a) or
            (a < 0 and abs(a) > b)
        ):
            result |= self._tmin

        return result
