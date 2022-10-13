import random


def main():
    print("Guess a number between 1 and 100: ")
    target_number = random.randint(1, 100)
    print(target_number)
    while True:
        user_guess = input("Enter your guess: ")
        if not number_valid(user_guess):
            continue
        if check_answer(int(user_guess), target_number):
            break


def number_valid(number):
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
