# main.py

from time import sleep
from hero import Hero
from minion import Minion, spawnminion
from utils import clear, game_over
from boss import boss
from store import store
from stats import stats, assign_stats

# Global dictionary to keep track of the bosses that have been defeated. At the start none of them have been defeated hence we initialize all values to False
boss_defeat = {1: False, 2: False, 3: False, 4: False}

# The create_player function will return a Hero object which will be the one ultimately controlled by the player.
def create_player():
    print("""
You will now start your adventure to defeat the Demon King and his three generals, they have started a war against humanity and seek to exterminate them. 
The Hero is the only one capable of stopping them. 
You will have to train, face enemies, level up and gather resources before taking on to the generals and finally the Demon King.
    """, flush=True)
    input("Press Enter to continue:")
    while True:
        clear()
        # Prompt the player for their name
        name = input("Let\'s start by getting your name.\nPlease type your name:\n")
        try:
            # We confirm with the player whether the name they wrote is right or not.
            clear()
            answer = input("The name you wrote is {name}. Is this the correct name? \n(Type Y for yes, or, N for no)\n".format(name = name)).upper().strip()
            match answer:
                case 'Y': break
                # If not we keep asking the player for their name.
                case 'N': 
                    print("Let\'s try that again shall we?\n")
                    input("Press Enter to continue")
                    continue
                # In case they write anything else.
                case _: 
                    print("Please type Y for yes, or, N for no. Other answers are not supported.")
                    input("Press Enter to continue")
                    continue
        # In case an ValueError happens.
        except ValueError :
            print("Sorry we didn\'t get that, please try again\n")
            input("Press Enter to continue")
            continue
    clear()
    print("{name} then, the outcome of your battles and how well you prepare yourself to face this challenge will forever change the destiny of humanity and the world.\n".format(name = name))
    input("Press Enter to continue")
    # Initial stat points. 
    stat_points = 10
    clear()
    print("""
Now is the time to distribute your initial stats you will receive {stat_points} for the start of your adventure. You will be able to distribute them in four different categories:
>  Attack: Determines how much damage you will deal to your enemies.
>  Defense: Determines how much damage reduction you will have against enemies.
>  Speed: Determines the chance of avoiding damage from an attack.
>  Crit Chance: Determines the chance of dealing extra damage when you attack an enemie.
    """.format(stat_points = stat_points))
    input("Press Enter to continue")
    while True:
        try:
            while True:
                clear()
                # We make sure that everytime we start this loop the stat_points is equal to 10.
                stat_points = 10
                attack_points = 0
                defense_points = 0
                speed_points = 0
                crit_points = 0
                print("Stat points remaining = {stat_points}\n".format(stat_points = stat_points))
                # We ask the player for the attack points he wants to get
                attack_points = int(input("Write the number of points you wish to invest towards ATTACK.\n"))
                # We check that the amount written is valid, if it is we reduce the total amount of points remaining.
                if attack_points > stat_points:
                    print("Calm down {name} you don't have that many points yet\n".format(name = name))
                    input("Press Enter to continue")
                    continue
                else:
                    stat_points -= attack_points
                # If the player doesn't have any more points to use we exit the loop.
                if stat_points == 0: break 
                clear()
                print("Stat points remaining = {stat_points}\n".format(stat_points = stat_points))
                # We ask the player for the defense points he wants to get
                defense_points = int(input("Write the number of points you wish to invest towards DEFENSE.\n"))
                # We check that the amount written is valid, if it is we reduce the total amount of points remaining.
                if defense_points > stat_points:
                    print("Calm down {name} you don't have that many points yet\n".format(name = name))
                    input("Press Enter to continue")
                    continue
                else:
                    stat_points -= defense_points
                # If the player doesn't have any more points to use we exit the loop.
                if stat_points == 0: break
                clear()
                # We ask the player for the speed points he wants to get
                print("Stat points remaining = {stat_points}\n".format(stat_points = stat_points))
                speed_points = int(input("Write the number of points you wish to invest towards SPEED.\n"))
                # We check that the amount written is valid, if it is we reduce the total amount of points remaining.
                if speed_points > stat_points:
                    print("Calm down {name} you don't have that many points yet\n".format(name = name))
                    input("Press Enter to continue")
                    continue
                else:
                    stat_points -= speed_points
                # If the player doesn't have any more points to use we exit the loop.
                if stat_points == 0: break
                clear()
                # We ask the player for the crit chance he wants to get
                print("Stat points remaining = {stat_points}\n".format(stat_points = stat_points))
                crit_points = int(input("Write the number of points you wish to invest towards CRIT CHANCE.\n"))
                # We check that the amount written is valid, if it is we reduce the total amount of points remaining.
                if crit_points > stat_points:
                    print("Calm down {name} you don't have that many points yet\n".format(name = name))
                    input("Press Enter to continue")
                    continue
                else:
                    stat_points -= crit_points
                break       
        except ValueError:
            print("Please use only numbers to select your stats\n")
            input("Press Enter to continue")
        clear()
        # Show the player the results of what he chose and ask him if he wants to keep it like that.
        print("This is how everything looks:\n")
        print(f'{"Attack":12}  ==>  {attack_points:3d}')
        print(f'{"Defense":12}  ==>  {defense_points:3d}')
        print(f'{"Speed":12}  ==>  {speed_points:3d}')
        print(f'{"Crit. Chance":12}  ==>  {crit_points:3d}')
        while True:
            answer = input("Confirm if this is okay \n(Type Y for yes, or, N for no)\n".format(name = name)).upper().strip()
            match answer:
                case 'Y': break
                # If not we repeat the attributes to 0 and ask the player again how he will like to distribute his initial stat points.
                case 'N':
                    print("Let\'s try that again shall we?\n")
                    input("Press Enter to continue")
                    break
                # In case they write anything else.
                case _: 
                    print("Please type Y for yes, or, N for no. Other answers are not supported.") 
                    continue
        if answer == 'N': continue
        clear()
        print("Thanks {hero}, your adventure will now start, your will be transported to the village where you will be able to choose what to do next. if you have any unused stat points left you will be able to use them there too.\nI wish you the best of luck in your journey!".format(hero = name))
        input('Press Enter to continue')
        break

    # Create player once we have all his information collected:
    return(Hero(name, attack_points, defense_points, speed_points, crit_points, stat_points))

# Message shown at the beginning of the game.
def welcome_message():
    print ("""

 ___       __    _______    ___        ________   ________   _____ ______    _______      
|\  \     |\  \ |\  ___ \  |\  \      |\   ____\ |\   __  \ |\   _ \  _   \ |\  ___ \     
\ \  \    \ \  \\ \   __/| \ \  \     \ \  \___| \ \  \|\  \\ \  \\\__\ \  \\ \   __/|    
 \ \  \  __\ \  \\ \  \_|/__\ \  \     \ \  \     \ \  \\\  \\ \  \\|__| \  \\ \  \_|/__  
  \ \  \|\__\_\  \\ \  \_|\ \\ \  \____ \ \  \____ \ \  \\\  \\ \  \    \ \  \\ \  \_|\ \ 
   \ \____________\\ \_______\\ \_______\\ \_______\\ \_______\\ \__\    \ \__\\ \_______\
    \|____________| \|_______| \|_______| \|_______| \|_______| \|__|     \|__| \|_______|
                                                                                          
                                                                                          
                                                                                          


    """, flush = True)

    sleep(0.75)

    print("""
    
 
 _________    ________     
|\___   ___\ |\   __  \    
\|___ \  \_| \ \  \|\  \   
     \ \  \   \ \  \\\  \  
      \ \  \   \ \  \\\  \ 
       \ \__\   \ \_______\
        \|__|    \|_______|
                           
                           
                           

    """, flush = True)

    sleep(0.75)

    print("""

 
 ________     ___    ___  _________    ___  ___      ________      ________           ________      ________    ________     
|\   __  \   |\  \  /  /||\___   ___\ |\  \|\  \    |\   __  \    |\   ___  \        |\   __  \    |\   __  \  |\   ____\    
\ \  \|\  \  \ \  \/  / /\|___ \  \_| \ \  \\\  \   \ \  \|\  \   \ \  \\ \  \       \ \  \|\  \   \ \  \|\  \ \ \  \___|    
 \ \   ____\  \ \    / /      \ \  \   \ \   __  \   \ \  \\\  \   \ \  \\ \  \       \ \   _  _\   \ \   ____\ \ \  \  ___  
  \ \  \___|   \/  /  /        \ \  \   \ \  \ \  \   \ \  \\\  \   \ \  \\ \  \       \ \  \\  \|   \ \  \___|  \ \  \|\  \ 
   \ \__\    __/  / /           \ \__\   \ \__\ \__\   \ \_______\   \ \__\\ \__\       \ \__\\ _\    \ \__\      \ \_______\
    \|__|   |\___/ /             \|__|    \|__|\|__|    \|_______|    \|__| \|__|        \|__|\|__|    \|__|       \|_______|
            \|___|/                                                                                                          
                                                                                                                             
                                                                                                                             


    """, flush = True)

    sleep(0.5)

    input("Press Enter to continue:")    

# Where the magic starts.
def village():
    # Printing a welcome message for the player:
    welcome_message()
    clear()
    # We create our player:
    hero = create_player()
    clear()
    # Explaining the menu to the player.
    print ("Welcome to the village {name} here you can choose between 4 different options".format(name = hero.name))
    print(f'{"Training":12}  ==>  {"This is how you level up and get money"}')
    print(f'{"Store":12}  ==>  {"Here you can get potions"}')
    print(f'{"Stats":12}  ==>  {"Here you can see your stats and use your stats points"}')
    print(f'{"Battle Boss":12}  ==>  {"Here you can battle the 3 generals and the demon king. (One at a time)"}')
    input("Press Enter to continue")
    clear()
    while True:
        # Whenever the hero returns to the village he recovers his health.
        hero.health = hero.maxhealth
        # We check if the player has defeated all the bosses of the game with the game_over function.
        game_over(hero, boss_defeat)
        try:
            # Prompt the player on what he wants to do now.
            decision = int(input("Where do you want to go now {hero}?\n1. Training grounds\n2. Store\n3. Check my stat points\n4. Battle Boss\n5. Exit\n".format(hero = hero.name)))
            match decision:
                case 1:
                    # Take the player to fight minions.
                    hero.train()
                case 2:
                    # Take the player to the store where he can buy potions.
                    store(hero)
                    clear()
                case 3:
                    # Take the player to check his stats and spend stats points if he wants to.
                    stats(hero)
                case 4:
                    # Take the player to fight the bosses of the game.
                    boss(hero, boss_defeat)
                    pass
                case 5:
                    # If the player decided to leave the game we thank him for playing and exit the program.
                    print("Thanks for playing!")
                    sleep(1)
                    clear()
                    exit()
                case _:
                    # If the player chooses another number print the menu again.
                    clear()
        except ValueError:
            # If the player writes something that is not a number then we show him this message.
            print("That is not a valid option try again.")
            clear()

# Start the game
village()
