from cs50 import get_float


def main():

    cents = get_money()

    quarters = calculate_quarters(cents)
    cents = cents - quarters * 25

    dimes = calculate_dimes(cents)
    cents = cents - dimes * 10

    nickels = calculate_nickels(cents)
    cents = cents - nickels * 5

    pennies = calculate_pennies(cents)
    cents = cents - pennies * 1

    print(quarters + dimes + nickels + pennies)


def get_money():
    try:
        while True:
            money = get_float("Change owed: ")
            if money < 0.00:
                print("Only positive numbers")
            else:
                break
    except ValueError:
        print("Invalid input")
    return money * 100


def calculate_quarters(cents):

    coins = 0
    if (cents % 25 == 0):
        coins = cents / 25
    else:
        while (cents > 25):
            cents -= 25
            coins += 1
    return coins


def calculate_dimes(cents):

    coins = 0

    if (cents % 10 == 0):
        coins = cents / 10
    else:
        while (cents > 10):
            cents -= 10
            coins += 1
    return coins


def calculate_nickels(cents):

    coins = 0

    if (cents % 5 == 0):
        coins = cents / 5
    else:
        while (cents > 5):
            cents -= 5
            coins += 1
    return coins


def calculate_pennies(cents):

    coins = 0

    while (cents > 0):
        cents -= 1
        coins += 1
    return coins


if __name__ == "__main__":
    main()
