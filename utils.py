# utils.py

from os import system, name
from time import sleep

# Function to clean the windows command prompt to keep everything more organized.
def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

# Function to check if the game is over.
def game_over(hero, boss_defeat):
    # If the final boss has been defeated, congratulate the player and end the game.
    if boss_defeat[4] == True:
        try:
            with open('winner.txt', 'w') as f:
                f.write ("Congratulations {name}\n\nThis txt was created as proof of you finishing the game!\nYour final stats:\n\nAttack: {attack}\nDefense: {defense}\nSpeed: {speed}\nCrit Chance: {critchance}\nMonsters defeated: {monsters}\nPotions used: {potions}".format(name = hero.name, attack = hero.attack, defense = hero.defense, speed = hero.speed, critchance = hero.critchance, monsters = hero.monsterskilled, potions = hero.potionsused))
        except FileExistsError as e:
            print(e)
        clear()
        print("You...", flush = True, sep= " ") 
        sleep(1.5)
        print("you have done it {hero}.".format(hero = hero.name), flush= True)
        sleep(2)
        print("You faced dangers like no other with courage and determination.", flush = True)
        input("Press Enter to continue.")
        clear()
        print("On your journey you defeated {monsters} monsters.".format(monsters = hero.monsterskilled), flush = True) 
        sleep(1.5)
        print("The 3 generals of the army.", flush= True)
        sleep(1.5)
        print("And the Demon King itself.", flush= True)
        input("Press Enter to continue.")
        clear()
        print("Your efforts have brought peace to this land, its inhabitants today celebrate and chant your name which will go down in history for generations.", flush = True)
        sleep(2.5)
        print("Your long journey ends here", flush = True)
        sleep(1.5)
        print("Thanks for everything.", flush = True)
        sleep(1.5)
        input("Press Enter to finish the game.")
        system('start winner.txt')
        system('start https://youtu.be/ym_jVTcBxSU')
        exit()