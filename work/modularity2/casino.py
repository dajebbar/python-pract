from random import randrange
from math import ceil


def roulette(money_bet, choice):
    money_bet_status = 0
    nbr = randrange(1, 51)
    # print(nbr)
    if choice == nbr:
        money_bet_status = money_bet * 3
    elif choice % 2 == 0 and nbr % 2 == 0:
        money_bet_status = money_bet / 2
    elif choice % 2 != 0 and nbr % 2 != 0:
        money_bet_status = money_bet / 2
    else:
        money_bet_status += money_bet

    return money_bet_status


if __name__ == "__main__":
    play = True

    while play:
        try:
            money_bet = int(input("Please enter your money stake >>> "))
            choice = int(input("Please choose a number between 1 and 50 >>> "))
            if money_bet <= 0 or choice < 1 or choice > 50:
                raise ValueError(
                    "Money should be positive and choice should be in range [1-50]")
        except ValueError as ve:
            print(ve)

        else:
            res = roulette(money_bet, choice)
            if res == 3 * money_bet:
                print(
                    f"GREAT! You W0N three times the amount wagered! ${ceil(res)}")
            elif res == money_bet / 2:
                print(f"Not bad! You kept half of your stake! ${ceil(res)}")
            else:
                print(f"No chance! you lost the bet! ${ceil(res)}")

        res = input("Would you like to play again? Tape [y/n] >>> ")
        if res == 'N' or res == 'n':
            play = False
