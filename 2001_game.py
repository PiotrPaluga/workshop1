from random import randint


def roll():
    """Simple function to roll 2 random numbers in range 1 - 6

    :rtype: int
    :return: sum of 2 random numbers"""
    return randint(1, 6) + randint(1, 6)


def game_2001():
    """Main function of our program"""
    p1_score = 0
    p2_score = 0

    while p1_score < 2001 and p2_score < 2001:
        roll1 = roll()
        roll2 = roll()
        print(f'Player 1 toss {roll1}')
        print(f'Player 2 toss {roll2}')
        # Player 1 score counter
        if roll1 == 7 and p1_score != 0:
            p1_score = p1_score // 7
            print(f'Player 1 score is divide by 7')
        elif roll1 == 11 and p1_score != 0:
            p1_score = p1_score * 11
            print(f'Player 1 score is multiply by 11')
        else:
            p1_score += roll1
        print(f'Player 1 score is {p1_score}')
        # Player 2 score counter
        if roll2 == 7 and p2_score != 0:
            p2_score = p2_score // 7
            print(f'Player 2 score is divide by 7')
        elif roll2 == 11 and p2_score != 0:
            p2_score = p2_score * 11
            print(f'Player 2 score is multiply by 11')
        else:
            p2_score += roll2
        print(f'Player 2 score is {p2_score}')

        input("Press ENTER to roll the dices")

    if p1_score >= 2001:
        print("Player 1 won!")
    elif p2_score >= 2001:
        print("Player 2 won!")
    else:
        print("Draw!")
    return "end"


if __name__ == '__main__':
    game_2001()
