# stats.py

from utils import clear

def stats(hero):
    clear()
    # Print the current stats of the hero.
    print(hero)
    # If the player doesn't have any stat points then take him back to the village after showing him his current stats.
    if hero.statpoints == 0:
        print("\nYou don't have any statpoints to spend right now.\n")
        input("Press Enter to return to the village.")
        clear()
    # If not then show him how many stat points he has.
    else:
        while True:
            try:
                # Ask the player if he wants to spend his stats points now.
                answer = input("You have {statpoints} statpoints available to use.\nDo you want to spend them now? Y/N\n".format(statpoints = hero.statpoints)).upper().strip()
                match answer:
                    case 'Y':
                        # If the player answer Y then call the assign_stats function.
                        assign_stats(hero)
                        break
                    case 'N':
                        # If the player answer N then leave the loop.
                        clear()
                        break
                    # In case they write anything else. we continue asking until they answer Y or N
                    case _: 
                        print("Please type Y for yes, or, N for no. Other answers are not supported.") 
                        continue
            except ValueError:
                # In case the player types anything that the interpreter considers a value error.
                print("\nWe didn't get that, please try again.")

def assign_stats(hero):
    while True:
        clear()
        print(f'{"Stat Points":12}  ==>  {hero.statpoints:3d}')
        print(f'{"Attack":12}  ==>  {hero.attack:3d}')
        print(f'{"Defense":12}  ==>  {hero.defense:3d}')
        print(f'{"Speed":12}  ==>  {hero.speed:3d}')
        print(f'{"Crit. Chance":12}  ==>  {hero.critchance:3d}')
        try:
            # We get the attribute that the player wants to upgrade.
            attribute = int(input("Select the attribute you want to upgrade:\n1. Attack\n2. Defense\n3. Speed\n4. Crit Chance\n5. Go back to the Village\n"))
            # Depending on the attribute that the player chooses different portion of the code is executed.
            match attribute:
                case 1:
                    # In case the player selects attack, check that the attribute is not at its max level.
                    if hero.attack == 10:
                        # If it is let the player know he can't upgrade this attribute anymore.
                        print("\nYou have already maxed out this stat, please choose another one.\n")
                        input("\nPress Enter to continue\n")
                        continue
                    try:
                        # If not ask how many stat points he wants to invest in this attribute.
                        upgrade_stats = int(input("How many points do you want to spend increasing your attack stats?\n"))
                        # If he writes a number bigger than the amount of points he has then let him know he doesn't have that amount of stat points available.
                        if upgrade_stats > hero.statpoints:
                            print("\nYou don't have that many stat points please try again.\n")
                            input("\nPress Enter to continue\n")
                            continue
                        # If he has the amount of points then increase the stats of the player on the selected attribute.
                        increase_stats(upgrade_stats, attribute, hero)
                    except ValueError:
                        print("\nWe didn't get that, please try again.\n")
                        input("\nPress Enter to continue\n")
                case 2:
                    # In case the player selects defense, check that the attribute is not at its max level.
                    if hero.defense == 10:
                        # If it is let the player know he can't upgrade this attribute anymore.
                        print("\nYou have already maxed out this stat, please choose another one.\n")
                        input("\nPress Enter to continue\n")
                        continue
                    try:
                        # If not ask how many stat points he wants to invest in this attribute.
                        upgrade_stats = int(input("How many points do you want to spend increasing your defense stats?\n"))
                        # If he writes a number bigger than the amount of points he has then let him know he doesn't have that amount of stat points available.
                        if upgrade_stats > hero.statpoints:
                            print("\nYou don't have that many stat points please try again.\n")
                            input("\nPress Enter to continue\n")
                            continue
                        # If he has the amount of points then increase the stats of the player on the selected attribute.
                        increase_stats(upgrade_stats, attribute, hero)
                    except ValueError:
                        print("\nWe didn't get that, please try again.\n")
                        input("\nPress Enter to continue\n")
                case 3:
                    # In case the player selects speed, check that the attribute is not at its max level.
                    if hero.speed == 10:
                        # If it is let the player know he can't upgrade this attribute anymore.
                        print("\nYou have already maxed out this stat, please choose another one.\n")
                        input("\nPress Enter to continue\n")
                        continue
                    try:
                        # If not ask how many stat points he wants to invest in this attribute.
                        upgrade_stats = int(input("How many points do you want to spend increasing your speed stats?\n"))
                        # If he writes a number bigger than the amount of points he has then let him know he doesn't have that amount of stat points available.
                        if upgrade_stats > hero.statpoints:
                            print("\nYou don't have that many stat points please try again.\n")
                            input("\nPress Enter to continue\n")
                            continue
                        # If he has the amount of points then increase the stats of the player on the selected attribute.
                        increase_stats(upgrade_stats, attribute, hero)
                    except ValueError:
                        print("\nWe didn't get that, please try again.\n")
                        input("\nPress Enter to continue\n")
                case 4:
                    # In case the player selects crit chance, check that the attribute is not at its max level.
                    if hero.critchance == 10:
                        # If it is let the player know he can't upgrade this attribute anymore.
                        print("You have already maxed out this stat, please choose another one.")
                        input("\nPress Enter to continue\n")
                        continue
                    try:
                        # If not ask how many stat points he wants to invest in this attribute.
                        upgrade_stats = int(input("How many points do you want to spend increasing your crit chance stats?\n"))
                        # If he writes a number bigger than the amount of points he has then let him know he doesn't have that amount of stat points available.
                        if upgrade_stats > hero.statpoints:
                            print("\nYou don't have that many stat points please try again.\n")
                            input("\nPress Enter to continue\n")
                            continue
                        # If he has the amount of points then increase the stats of the player on the selected attribute.
                        increase_stats(upgrade_stats, attribute, hero)
                    except ValueError:
                        print("\nWe didn't get that, please try again.\n")
                        input("\nPress Enter to continue\n")
                case 5:
                    # Take the player back to the village if he chooses to.
                    print("Going back to the Village!", flush=True)
                    input('Press Enter to continue')
                    clear()
                    break
                case _:
                    # In case the player selects a not supported number.
                    print("\nNot a valid option, please try again.\n")
                    input("\nPress Enter to continue\n")
                    continue
        except ValueError:
            # In case the player writes something that is not a number.
            print("\nWe didn't get that, please try again.")
            input("\nPress Enter to continue\n")

def increase_stats(points, attribute, hero):
    # Depending on the selected attribute increase the stat by the selected amount
    # If the amount was to surpass 10 which is the max level for each attribute then set the attribute to 10 and return any unused points so that the player can assign them to other attribute.
    match attribute:
        case 1:
            attack_before = hero.attack
            hero.attack += points
            if hero.attack > 10: 
                hero.attack = 10
                print("\nYou have maxed out this stat! We'll leave it at 10 and return any unused points.\n")
                input("\nPress Enter to continue\n")
            hero.statpoints -= (hero.attack - attack_before)
            print("\nDone!\n")
            input("\nPress Enter to continue\n")
        case 2:
            def_before = hero.defense
            hero.defense += points
            if hero.defense > 10: 
                hero.defense = 10
                print("\nYou have maxed out this stat! We'll leave it at 10 and return any unused points.\n")
                input("\nPress Enter to continue\n")
            hero.statpoints -= (hero.defense - def_before)
            print("\nDone!\n")
            input("\nPress Enter to continue\n")
        case 3:
            speed_before = hero.speed
            hero.speed += points
            if hero.speed > 10: 
                hero.speed = 10
                print("\nYou have maxed out this stat! We'll leave it at 10 and return any unused points.\n")
                input("\nPress Enter to continue\n")
            hero.statpoints -= (hero.speed - speed_before)
            print("\nDone!\n")
            input("\nPress Enter to continue\n")
        case 4:
            crit_before = hero.critchance
            hero.critchance += points
            if hero.critchance > 10: 
                hero.critchance = 10
                print("\nYou have maxed out this stat! We'll leave it at 10 and return any unused points.\n")
                input("\nPress Enter to continue\n")
            hero.statpoints -= (hero.critchance - crit_before)
            print("\nDone!\n")
            input("\nPress Enter to continue\n")