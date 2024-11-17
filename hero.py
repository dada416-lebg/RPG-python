# hero.py

from random import randint, random
from time import sleep
from minion import Minion, spawnminion
from utils import clear

# Global dictionary to keep track of the bosses that have been defeated. At the start none of them have been defeated hence we initialize all values to False
boss_defeat = {1: False, 2: False, 3: False, 4: False}

# Object Hero which will ultimately be the player, will keep track of his stats, money, potions, monsters killed and potions used.
class Hero():
    def __init__(self, name, attack, defense, speed, critchance, statpoints):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.critchance = critchance
        self.statpoints = statpoints
        self.health = 10
        self.maxhealth = 10
        self.lvl = 0
        self.exp = 0
        self.money = 0
        self.potions = 0
        self.monsterskilled = 0
        self.potionsused = 0

    # Using the __repr__ function so that the player can check his current stats.
    def __repr__(self):
        print("You are the Hero {name}.".format(name = self.name))
        print("These are your current stats:\n\nLevel: {lvl}\nAttack: {attack}\nDefense: {defense}\nSpeed: {speed}\nCrit Chance: {critchance}\nExp: {exp}\n".format(lvl = self.lvl, attack = self.attack, defense = self.defense, speed = self.speed, critchance = self.critchance, exp = self.exp))
        print("You have {potions} potions".format(potions = self.potions))
        return ("\nYou have {money} money\n".format(money = self.money))

    # The train function will set up the combat logic for the player to fight against minions, depending on the player level different minions will appear
    def train(self):
        # Max lvl is 30. We let the player know that he won't be getting any more levels but he can still grind for potions and money.
        if self.lvl >= 30:
            print("\nYou are at max level so you won't level up anymore, but you can still get potions and money from the monsters you defeat.\n")
            input("Press Enter to continue.")
        # keep_fighting keeps track of whether the player wants to keep fighting more minions or go back to the village to spend stat points, buy potions, fight a boss or just recover his health.
        # As we enter the loop we set the variable to True.
        keep_fighting = True
        while keep_fighting == True:
            # We get a minion name from the minion list and create it using the spawnminion function to fight the hero.
            # Depending on the player level we will get stronger enemies.
            if self.lvl <= 10:
                minion = spawnminion(self.attack,self.defense, self.speed, self.critchance, self.maxhealth, 1)
            elif self.lvl > 10 and self.lvl <= 20:
                minion = spawnminion(self.attack,self.defense, self.speed, self.critchance, self.maxhealth, 2)
            elif self.lvl > 20:
                minion = spawnminion(self.attack,self.defense, self.speed, self.critchance, self.maxhealth, 3)
            ############################
            # Battle logic starts here #
            ############################
            clear()
            print("You have encountered a {minion} prepare to fight!\n".format(minion = minion.name))
            combat = True
            while combat == True:
                try:
                    # We let the player know how much hp he has and how many potions he was at the beggining of this turn.
                    print(f'{"HP:":7}  {"{health}/{maxhealth}"}'.format(health = self.health, maxhealth = self.maxhealth))
                    print(f'{"Potions:":7}  {"{potions}"}'.format(potions = self.potions))
                    # We ask the player if he wants to attack or drink a potion.
                    decision = int(input('\nIt\'s your turn {hero} what do you want to do?\n1. Attack\n2. Use potion\n'.format(hero = self.name)))
                    match decision:
                        case 1:
                            clear()
                            # If the player chooses 1 then we start the combat by attacking the minion using the attack_enemy method.
                            combat = self.attack_enemy(minion)
                            # If the minion has any HP left the attack enemy function will return True in which case it's the minion's turn
                            if combat == True:
                                # The minion attacks the player.
                                print("\nCarefull {enemy} is attacking now!\n".format(enemy = minion.name))
                                # If the player has no more hp after the damage calculation then combat will be set to False and the Hero will be returned to the village.
                                combat = minion.attack_hero(self)
                            # If the minion does not have any HP left it means the player won the combat.
                            else:
                                del minion
                                # Increase the counter of how many monsters the player has killed.
                                self.monsterskilled += 1
                                # Give the player experience for winning the combat.
                                self.exp += 5
                                # If the player is at his max level he won't get any more exp points.
                                if self.lvl == 30: self.exp = 0
                                # Give the player 1 to 3 $ for winning the combat.
                                self.money += randint(1,3)
                                # Tell the player how many money he has now
                                print ("You got {money}$ now.\n".format(money = self.money))
                                # The player has 1/4 chances of getting some potions if he doesn't have the maximum amount of potions already (10)
                                if (random()*100 < 25 and self.potions < 10):
                                        # The player could get one or two potions from the minion.
                                        random_potions = randint (1, 2)
                                        print("What's that? It seems like the monster was carrying some potions.\n\nYou got {potions} more potion(s)".format(potions = random_potions))
                                        # Add the potions that the minion left to the player potions
                                        self.potions += random_potions
                                        if self.potions > 10: 
                                            self.potions = 10
                                            print("\n\nYou have got the maximum amount of potions you will have to leave some behind.\n")
                                # When the player hits 10 exp we will get a new level and reset his exp. The level_up method manages this.
                                if self.exp >= 10:
                                    self.level_up()

                        case 2:
                            clear()
                            # If the player choose to use a potion we call the use_potion method.
                            self.use_potion()
                        case _:
                            # In case the player writes a number other than 1 or 2
                            print("Please type only 1 or 2 on your keyboard to choose an option.")
                            continue
                except ValueError:
                    # In case the player writes a value that is not a number
                    print("Sorry we didn't get that please try again.")
            # If the player has no more hp left then leave the combat logic.
            if self.health == 0: break
            # Keep asking the player what he wants to do until he chooses a valid answer.
            while True:
                try:
                    # Ask the player whether he wants to continue fighting or go back to the village.
                    decision = int(input('You have {health}/{maxhealth} HP remaining and {potions} potions, do you wish to continue training or you want to go back to the village?\n1. Continue training\n2. Go back.\n'.format(health = self.health, maxhealth = self.maxhealth, potions = self.potions)))
                    match decision:
                        # If the player selects to keep fighting set keep_fighting to True and break the current loop as a decision was made.
                        case 1:
                            keep_fighting = True
                            break
                        case 2:
                        # If the player selects to go back to the village set keep_fighting as False and break the current loop as a decision was made.
                            keep_fighting = False
                            clear()
                            print("Going back to the village now.", flush= True)
                            input("Press Enter to continue.")
                            clear()
                            break
                        case _:
                        # In case the player writes a number other than 1 or 2.
                            print("Please type only 1 or 2 on your keyboard to choose an option.")
                            continue
                except ValueError:
                    # In case the player writes a value that is not a number.
                    print("Sorry we didn't get that please try again.")
    # The level_up method will level up the player when he gets 10 or more exp and cap the mas level at level 30.
    def level_up(self):
        # While the player has more than 10 exp, increase the level by one current health by 3 max health by 5 and reduce exp by 10
        while self.exp >= 10:
            self.lvl += 1
            # If the player already reached level 30 he won't get any more levels or stats.
            if self.lvl > 30:
                print("You have reached the maximum level you can get {hero}".format(hero = self.name))
                self.lvl = 30
                self.exp = 0
                return 0
            self.health += 3
            self.maxhealth += 5
            self.exp -= 10
            self.statpoints += 1
            # Let the player know he has leveled up.
            print ("\nYou leveled up {hero}! you are now level {lvl} and have {statpoints} stat points available to use when you go back to the village\n\nYou have recovered 3 health points and have 5 more maximum health points.\n".format(hero = self.name, lvl = self.lvl, statpoints = self.statpoints))

    def use_potion(self):
        # Uses a potion on the hero to recover 20% of his health. (If he has potions left.)
        if self.potions > 0:
            while True:
                # If the hero is at it's current maximum HP inform him about it.
                if self.health == self.maxhealth:
                    print('You already have all your HP {name}'.format(name = self.name))
                    return False
                else:
                # If we get here we give the potion to the hero and reduce the amount of potions that he has by 1
                    self.gainhealth()
                    self.potions -= 1
                    self.potionsused += 1
                    return True
                    break
        # If the player doesn't have potions, inform him about it and leave the method.
        else: print('You don\'t have any potions left.'); return False

    def gainhealth(self):
        # Recover 20% of the maximum health.
        self.health += round(self.maxhealth * 0.2)
        # If the amount of health was to exceed the amount of maximum health we make the current health equal to the maximum health.
        if self.health > self.maxhealth:
            self.health = self.maxhealth
        # Let the player know the potion was used and how much HP he has now.
        print('You used a potion and have now {health}/{maxhealth} HP'.format(health = self.health, maxhealth = self.maxhealth))

    def attack_enemy(self, enemy):
        # dodge will be set to True if the enemy dodged the attack or false if it did not.
        dodge = enemy.dodge()
        # If he dodges no damage calculation is made.
        if dodge:
            print("\n{enemy} is too fast!, he dodged your attack.\n".format(enemy = enemy.name))
            return True
        # If he did not dodge we make damage to the enemy
        else:
            # crit method will return 1 or 2 randomly. the higher your critchange the higher the chance of getting a crit.
            crit = self.crit()
            # If crit is equal to 2 the damage will be doubled.
            return (enemy.lose_health(round((self.maxhealth * 0.75 + self.attack) - (enemy.maxhealth * 0.5 + enemy.defense))*crit))

    def crit(self):
        # At max critchance (10) the player will have a 50% chance of hitting a crit strike.
        if (random()*100 < self.critchance * 5):
            # If the random number generated between 0 and 100 is lower than the players critchance then he lands a critical strike
            print("\nYou land a critical strike!\n")
            return 2
        return 1
    def dodge(self):
        # At max speed (10) the player will have a 33% chance of dodging an enemy attack.
        if ((random()*100) < self.speed*3.3):
            # If the random number generated between 0 and 100 is lower than the players speed then he dodges the enemy attack.
            return True
        return False
    def lose_health(self, damage):
        # Added check so that negative damages are not possible. And you always lose at least 1 health.
        if damage <= 0:
            damage = 1
        print("\nYou take {damage} damage!\n".format(damage = damage))
        # We reduce the amount of health of the player by the amount of damage taken.
        self.health -= damage
        # We check that the health never goes lower than 0. If the health hits 0 then the player has been defeated. Take 25% of his money and all his potions. Return False to end the combat.
        if self.health <= 0:
            self.health = 0
            # We inform the player that he has lost and will be transported back to the village with less money and no potions.
            print("\nYou have been defeated!\nYou will be transported back to the village and lose some money and your potions.")
            self.potions = 0
            self.money -= round(self.money * 0.25)
            input("\nPress Enter to continue\n")
            clear()
            return False
        # If the player has HP remaining then let him know how much HP he has left and continue with the combat returnint True.
        else:
            print ("\nYou have {health}/{maxhealth} points remaining\n".format(health = self.health, maxhealth = self.maxhealth))
            return True