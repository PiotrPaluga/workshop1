def get_answer():
    possible_input = ['too big', 'too small', 'you win']
    while True:
        answ = input("Did i guessed? (write: 'too big', 'too small, lub 'you win')").lower()
        if answ in possible_input:
            break
        print("Wrong input")
    return answ


def guess_the_num():
    print("Think about number from 0 to 1000 and i will guess it within 10 attempts")
    print("press ENTER to continue")
    input()
    min_num = 0
    max_num = 1000
    user_ans = ""
    while user_ans != "you win":
        guess = (max_num - min_num) // 2 + min_num
        print(f'Your number is: {guess}')
        user_ans = get_answer()
        if user_ans == 'too big':
            max_num = guess
        elif user_ans == 'too small':
            min_num = guess

    print("Hurra! I guessed!")


if __name__ == '__main__':
    guess_the_num()
