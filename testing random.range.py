import random

def slots(money):
    required_funds = 4
    if money >= required_funds:
        random_num = random.randrange(0,100,1)
        if random_num >= 70:
            money += 20
            print("You won a game of slots! Congrats! 20 dollars has been added to your account")
        else:
            money -= required_funds
            print("thank you for playing Slots, shocking you didn't win anything")
    else:
        print("Sorry, insufficient funds")
    return money 

def main():
    money = int(input("How much money do you want to enter the casino with?"))
    while money > 0:
        print("Your balance is $" + str(money))
        print("1. Slots")
        pick_game = str(input("Please select your choice above or select any other key to exit"))
        if pick_game == '1':
            money = slots(money)
        else:
            break
    print("You have managed to crawl out of the casino with $" + str(money))

main()