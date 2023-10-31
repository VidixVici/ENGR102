# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         YOUR NAME
# Zachary Harbert
# Cristian Briones
# Denzell Nieto
# Tanmai Buyyanapragada
# Section:      562
# Assignment:   9.15 LAB: Word puzzle
# Date:         25 October 2023


def print_puzzle(puzzle):
    """Print puzzle as a long division problem."""
    puzzle = puzzle.split(",")
    for i in range(len(puzzle)):
        if i == 1:
            print(f'{len(puzzle[i].split("|")[1]) * "_": >16}')
        print(f"{puzzle[i]: >16}")
        if i > 1 and i % 2 == 0:
            print(f"{'-'*len(puzzle[i]): >16}")


def get_valid_letters(puzzle):
    #result
    result = ""
    # go through the characters in the puzzle
    for char in puzzle:
        # Check if the character is a letter and not already in the result
        if char.isalpha() and char not in result:
            result += char
            # Check if we have found 10 unique letters
            if len(result) == 10:
                break
        # Check if we have found 10 unique letters
        if len(result) == 10:
            break
    # Return the result string
    return result


def is_valid_guess(valid_letters, user_guess):
    # MAKE SURE UPPERCASE
    valid_letters = valid_letters.upper()
    user_guess = user_guess.upper()

    # Check if the lengths of the guess and the valid letters are both 10
    if len(user_guess) == 10 and len(valid_letters) == 10:
        # Check if all characters in the guess are in the valid letters
        if all(char in valid_letters for char in user_guess):
            # Check if there are no repeated characters in the user's guess
            if len(set(user_guess)) == 10:
                return True

    return False


def check_user_guess(dividend, quotient, divisor, remainder):
    return dividend == (quotient * divisor + remainder)

"""
def make_number(word, user_guess):
    # CHARACTERS TO DIGITS ?
    char_to_digit = {char: str(i) for i, char in enumerate(user_guess)}

    # store the digits
    digits = ""

    # convert chars to digits
    for char in word:
        # If the character is in the dictionary, append its digit to the result
        if char in char_to_digit:
            digits += char_to_digit[char]
        else:
            return None

    # Convert the concatenated digits to an integer
    result = int(digits)
"""
def make_number(word, user_guess):
    char_to_digit = {char: str(i) for i, char in enumerate(user_guess)}
    digits = ""
    
    # Convert the characters in the word to their corresponding digits and build the integer
    for char in word:
        if char in char_to_digit:
            digits += char_to_digit[char]
    
    integer_equivalent = int(digits)
    
    return integer_equivalent


if __name__ == "__main__":
    main()
