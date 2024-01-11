from random import randint


def get_number():
    """Get number from user.

    Try until user gives a proper number
    :rtype: int
    :return: given number as int
    """
    while True:
        try:
            number = int(input("Guess the number:"))
            break
        except ValueError:
            print("This is not a number!")
    return number


def guess_the_number():
    """Main function of our program."""

    number_to_guess = randint(1, 100)
    guessed_number = get_number()
    while number_to_guess != guessed_number:
        if guessed_number < number_to_guess:
            print("Too small!")
        else:
            print("too big!")
        guessed_number = get_number()
    print("You win!")


if __name__ == '__main__':
    guess_the_number()