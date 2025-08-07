# Power Digit Sum
# Problem 16
#
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?

def power_digit_sum(base: int, exponent: int) -> int:
    """
    Calculates the sum of the digits of a number raised to a power.
    """
    number = pow(base, exponent)
    return sum(int(digit) for digit in str(number))

if __name__ == '__main__':
    # For 2^15, the answer is 26.
    print(f"The sum of digits for 2^15 is: {power_digit_sum(2, 15)}")
    # For 2^1000, which is the problem to solve.
    print(f"The sum of digits for 2^1000 is: {power_digit_sum(2, 1000)}")
