import random

from tkinter import * 

root = Tk()
root.title("Daniel's Casino")
root.geometry('350x200')
root.mainloop()

def slots(money):
    required_funds = 4
    if money >= required_funds:
        random_num = random.randrange(0,100,1)
        if random_num >= 85:
            money += 20
            print("You won a game of slots! Congrats! 20 dollars has been added to your account"+"\n")
        else:
            money -= required_funds
            print("thank you for playing Slots, you didn't win, but better luck next time!"+"\n")
    else:
        print("Sorry, insufficient funds")
    return money 

def roulette(money):
    required_funds = 10
    if money >= required_funds:
        random_num = random.randrange(0,100,1)
        if random_num >= 90:
            money += 50
            print("You won a game of Roulette! Congrats! 50 dollars has been added to your account"+"\n")
        else: 
            money -= required_funds
            print("Thank you for playing Roulette, you didn't win, but better luck next time!"+"\n")
    elif money >= 4:
        print("You can't afford this game, would you rather play slots?"+"\n")
        choice = input("Enter 'y' if you'd like to play the Slots one time. Otherwise, press any other key"+"\n")
        if choice == 'y':
            money = slots(money)
    else:
        print("Sorry, insufficient funds"+"\n")
    return money

def main():
    money = int(input("How much money do you want to enter the casino with?"+"\n"+"balance = "))
    while money > 0:
        print("Your balance is $" + str(money)+"\n")
        print('''
        1. Slots $4 to play
        2. Roulette $10 to play
        Rules: 
        - Slots has a 15 percent chance of winning $20, but it costs $4
        - Roulette has a 10 percent chance of winning $50 ''')
        print("\n")
        pick_game = str(input("Please select your choice above or select any other key to exit"+"\n"+"choice = "))
        if pick_game == '1':
            money = slots(money)
        elif pick_game == '2': 
            money = roulette(money)
        else:
            break
    print("You have managed to crawl out of the casino with $" + str(money))

main()