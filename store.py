# store.py
from utils import clear
def store(hero):
    while True:
        clear()
        # Greet the player and let him know the price of the potions.
        print ("Welcome to the store {name} here you can buy potions for your adventures\n".format(name = hero.name))
        print (f'{"Item:":6}    {"Price:"}')
        print (f'{"Potion":6}    {"5$"}')
        try:
            # Ask the player how many potions he wants to buy
            potions_to_buy = int(input("\nYou have {potions} potions and {money}$, how many potions would you like to buy?\n\nWrite 0 if you want to go back to the village\n".format(potions = hero.potions, money = hero.money)))
            # If the player writes 0 we take him back to the village
            if potions_to_buy == 0:
                print("\nWe hope to have you back soon!")
                input("Press Enter to go back to the Village.\n")
                break
            # We set a maximum amount of potions so that the player can't just buy them infinitely
            if potions_to_buy > 10: potions_to_buy = 10; print("\nYou can't carry more than 10 potions we will assume you want 10 potions\n")
            # If the player set an amount that is going to go over 10 potions we max out his number of potions to 10 instead without making him pay extra money.
            if hero.potions + potions_to_buy > 10: potions_to_buy = potions_to_buy - hero.potions; print("\nYou don't have space on your inventory for that amount of potions, we will max out your potions to 10.\n")
            # Check whether the player has enough money to buy the requested potions.
            if (potions_to_buy * 5) > hero.money:
                print("\nYou don't have enough money to buy that many potions, please select a lower number.\n")
                input("Press Enter to go back to the Store.\n")
                continue
            # If the player has enough money then increase the amount of potions he has by the number he bought and reduce the money he has by the money he spent.
            else:
                hero.potions += potions_to_buy
                hero.money -= potions_to_buy * 5
                print("\nThanks for your purchase! you now have {potions} potions\nCome back soon!".format(potions = hero.potions))
                input("Press Enter to go back to the Village.\n")
                break
        except ValueError:
            print("\nThe value you wrote is not valid, please try again.\n")
            input("Press Enter to go back to the Store.\n")