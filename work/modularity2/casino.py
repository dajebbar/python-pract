from random import randrange
from math import ceil


def roulette(money_bet, choice):
    money_bet_status = 0
    nbr = randrange(50)
    print(nbr)
    if choice == nbr:
        money_bet_status = money_bet * 3
    elif choice % 2 == 0 and nbr % 2 == 0:
        money_bet_status = money_bet / 2
    elif choice % 2 != 0 and nbr % 2 != 0:
        money_bet_status = money_bet / 2
    else:
        money_bet_status -= money_bet

    return money_bet_status


res = roulette(30, 10)
print(res)
