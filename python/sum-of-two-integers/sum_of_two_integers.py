import sys


class Solution:
    def get_sum(self, a: int, b: int, max_bits) -> int:

        TMAX = 2**(max_bits - 1) - 1
        TMIN = -2**(max_bits - 1)

        if a > TMAX or a < TMIN:
            print(
                f"Error: signed integer '{a}' cannot be supported by "
                f"{max_bits} bits"
            )
            sys.exit(1)

        if b > TMAX or b < TMIN:
            print(
                f"Error: signed integer '{b}' cannot be supported by "
                f"{max_bits} bits"
            )
            sys.exit(1)

        bit_mask = 1
        carry = 0
        result = 0

        # we use XOR to sum each individual bits
        for _ in range(max_bits):
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
            result |= -2**(max_bits - 1)

        return result


def main(argc, argv):
    s = Solution()
    print(s.get_sum(-15, 16, 5))


if __name__ == "__main__":
    main(sys.argv, len(sys.argv))
