# boss.py

from random import randint
from utils import clear
from minion import spawnminion

# If the player chooses the boss function will execute.
def boss(hero, boss_defeat):
    leveldif = 0
    # We check the value for each key of the dictionary boss defeat and decide the boss to face depending on which one has not been defeated yet
    if boss_defeat[1] == False:
        boss_level = 4
        leveldif = -5
    elif boss_defeat[2] == False:
        boss_level = 5
        leveldif = 0
    elif boss_defeat[3] == False:
        boss_level = 6
        leveldif = 5
    elif boss_defeat[4] == False:
        boss_level = 7
        leveldif = 10
    minion = spawnminion(hero.attack + leveldif ,hero.defense + leveldif, hero.speed + leveldif, hero.critchance + leveldif , hero.maxhealth + leveldif, boss_level)
    match boss_level:
        # We print the boss name according to the level the player is facing.
        case 4:
            print("\nYou face the first general of the Demon King army: {name}, embrace yourself!\n".format(name = minion.name))
        case 5:
            print("\nYou face the second general of the Demon King army: {name}, embrace yourself!\n".format(name = minion.name))
        case 6:
            print("\nYou face the third general of the Demon King army: {name}, embrace yourself!\n".format(name = minion.name))
        case 7:
            print("\nYou face the Demon King himself: {name}, embrace yourself!\n".format(name = minion.name))
    combat = True
    while combat == True:
        try:
            # We let the player know how much hp he has and how many potions he was at the beginning of this turn.
            print(f'{"HP:":7}  {"{health}/{maxhealth}"}'.format(health = hero.health, maxhealth = hero.maxhealth))
            print(f'{"Potions:":7}  {"{potions}"}'.format(potions = hero.potions))
            # We ask the player if he wants to attack or drink a potion.
            decision = int(input('\nIt\'s your turn {hero} what do you want to do?\n1. Attack\n2. Use potion\n'.format(hero = hero.name)))
            match decision:
                case 1:
                    clear()
                    # If the player chooses 1 then we start the combat by attacking the minion using the attack_enemy method.
                    combat = hero.attack_enemy(minion)
                    # If the minion has any HP left the attack enemy function will return True in which case it's the minion's turn
                    if combat == True:
                        # The minion attacks the player.
                        print("\nCareful {enemy} is attacking now!\n".format(enemy = minion.name))
                        # If the player has no more hp after the damage calculation then combat will be set to False and the Hero will be returned to the village.
                        combat = minion.attack_hero(hero)
                    # If the minion does not have any HP left it means the player won the combat.
                    else:
                        del minion
                        # Mark the boss as defeated.
                        boss_defeat[boss_level - 3] = True
                        print("You have defeated {name}!".format(name = minion.name))
                        input("Press Enter to continue.")
                        clear()
                case 2:
                    clear()
                    # If the player chooses to use a potion we call the use_potion method.
                    hero.use_potion()
                case _:
                    # In case the player writes a number other than 1 or 2
                    print("Please type only 1 or 2 on your keyboard to choose an option.")
                    continue
        except ValueError:
            # In case the player writes a value that is not a number
            print("Sorry we didn't get that please try again.")
    # If the player has no more hp left then leave the combat logic.
    if hero.health == 0:
        print("You have been defeated by {name}!".format(name = minion.name))
        input("Press Enter to continue.")
        clear()