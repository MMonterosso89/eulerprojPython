# Number Letter Counts
# Problem 17
#
# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out
# in words, how many letters would be used?
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
# forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
# 20 letters. The use of "and" when writing out numbers is in compliance
# with British usage.

def number_to_words(n: int) -> str:
    """Converts a number from 1 to 1000 into its English word representation."""
    units = {
        0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
        7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven",
        12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
        16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"
    }
    tens = {
        2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty",
        7: "seventy", 8: "eighty", 9: "ninety"
    }

    if n == 1000:
        return "one thousand"

    words = ""
    if n >= 100:
        words += units[n // 100] + " hundred"
        if n % 100 != 0:
            words += " and "

    remainder = n % 100
    if remainder > 0:
        if remainder < 20:
            words += units[remainder]
        else:
            words += tens[remainder // 10]
            if remainder % 10 != 0:
                words += "-" + units[remainder % 10]
    return words

def count_letters(s: str) -> int:
    """Counts the letters in a string, ignoring spaces and hyphens."""
    return len(s.replace(" ", "").replace("-", ""))

def total_letter_count(limit: int) -> int:
    """
    Calculates the total number of letters used for numbers from 1 to limit.
    """
    total = 0
    for i in range(1, limit + 1):
        words = number_to_words(i)
        total += count_letters(words)
    return total

if __name__ == '__main__':
    # Test cases from the problem description
    print(f"Letters in 'one' to 'five': {total_letter_count(5)}")
    print(f"Letters in 342: {count_letters(number_to_words(342))}")
    print(f"Letters in 115: {count_letters(number_to_words(115))}")

    # Final answer
    print(f"Total letters from 1 to 1000: {total_letter_count(1000)}")
