from random import randint, shuffle


def get_number(x):
    """Get index of "x" number from user.

        Try until user gives a proper number
        :rtype: int
        :return: given number as int
        """
    while True:
        try:
            number = int(input(f'Podaj {x} liczbę'))
            break
        except ValueError:
            print("To nie jest liczba!")
    return number


def get_numbers():
    """Get 6 numbers from user.

    Try until gives proper numbers.
    :rtype: list
    :return: return list of 6 numbers from user."""
    given_numbers = []
    index = 1
    while len(given_numbers) < 6:
        new_number = get_number(index)
        if new_number not in given_numbers and 0 < new_number <= 49:
            given_numbers.append(new_number)
            index += 1
    return given_numbers


def show_numbers(numbers):
    """Print given number with ascending order.

    :param list numbers: sorted list of numbers"""
    print(", ".join(str(number) for number in sorted(numbers)))

def drawing_numbers():
    """Choose 6 random numbers.

    :rtype: list
    :return: return list of 6 random numbers"""
    numbers = list(range(1, 50))
    shuffle(numbers)
    return numbers[:6]


def lotto():
    """Main function of program"""
    user_numbers = get_numbers()
    print("Your numbers:")
    show_numbers(user_numbers)

    random_numbers = drawing_numbers()
    print("Lotto numbers:")
    show_numbers(random_numbers)

    hits = 0
    for number in user_numbers:
        if number in random_numbers:
            hits += 1

    print(f"You hit {hits} {'number' if hits == 1 else 'numbers'}!")


if __name__ == '__main__':
    lotto()
