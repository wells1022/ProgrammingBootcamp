"""
Programming Task #2
Create a game where the user must correctly guess a randomly generated integer between 1 and 100.

The user should be notified whether their guess was “lower” or “higher” than the target number.

Note that you will need to use the random library’s randint function.

Remember:
- Use functions to group code
- Try to have functions that only do one “thing” (e.g. print a message, validate user input, check what message to display)
- Check for invalid inputs, notifying the user and re-prompting for a valid input

"""

import random


def main():
    """Main ligic of tha game
        receive input and check result.
    """
    print("Guess a number between 1 and 100: ")
    target_number = random.randint(1, 100)
    while True:
        user_guess = input("Enter your guess: ")
        if not number_valid(user_guess):
            continue
        if check_answer(int(user_guess), target_number):
            break


def number_valid(number):
    """Check if the guess number is valid.

    Args:
        number (str): Guess from user

    Returns:
        bool: If guess is valid
    """
    if number == "":
        print("Input can't be empty")
        return False
    elif not number.isnumeric():
        print("Please enter a number")
        return False
    elif 1 > int(number) or int(number) > 100:
        print("Please enter a number between 1 and 100")
        return False
    else:
        return True


def check_answer(guess_int, target_number):
    """Check if the guess meets the target.

    Args:
        guess_int (int): User guess
        target_number (int): Target number

    Returns:
        bool: If guess meets the target
    """
    if guess_int < target_number:
        print("Guess is lower than target!")
        return False
    elif guess_int > target_number:
        print("Guess is higher than target!")
        return False
    else:
        print("Congratulations you win!")
        print(f"The target number is {guess_int}")
        return True


main()
