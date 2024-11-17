# minion.py

from random import randint, random

# List from where we will randomly get the name of the enemies the player will face while training.
minion_list = ['Slime', 'Wolf', 'Undead', 'Goblin', 'Bandit', 'Zombie', 'Ghoul', 
                'Orc', 'Dark Knight', 'Gremlin', 'Werewolf', 'Golem', 'Witch', 'Valkyrie',
                'Vampire', 'Chimera', 'Giant', 'Dragon', 'Minotaur', 'Devil', 'Manticore']

# All the enemies in the game including the bosses are Minion objects. what changes about them is how their stats are calculated when using the spawnminion function.
class Minion():
    def __init__(self, name, attack, defense, speed, critchance, health):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.critchance = critchance
        self.health = health
        self.maxhealth = health

    def __repr__(self):
        return("This minion is a {name}, Attack: {attack}, Defense: {defense}, Speed: {speed}, CritChance = {critchance}, HP = {hp}, Max HP = {maxhp}".format(name = self.name, attack = self.attack, defense = self.defense, speed = self.speed, critchance = self.critchance, hp = self.health, maxhp = self.maxhealth))

    # The dodge method will determine if the minion dodges or not the attack of the hero.
    def dodge(self):
        if ((random()*100) < self.speed*3.3):
            return True
        return False

    # The lose_health method will carry out the damage calculation in case the minion has no hp after the damage calculation it will return False to finish the combat logic, otherwise it will return True to continue with the combat logic.
    def lose_health(self, damage):
        # Adding a check so that negative damages are not possible and there is always at least 1 damage.
        if damage <= 0:
            damage = 1
        print("\n{minion} takes {damage} damage!\n".format(minion = self.name, damage = damage))
        self.health -= damage
        # If the health was going to be lower than 0 set it to 0 instead.
        if self.health <= 0:
            self.health = 0
            # Let the player know that the enemy has no hp and therefore has been defeated.
            print("\nYou have defeated {enemy}!\n".format(enemy = self.name))
            return False
        else:
            # If the enemy still has HP after the damage calculation then let the player know how much HP the minion has and continue with the combat.
            print ("\n{enemy} has {health}/{maxhealth} HP remaining\n".format(enemy = self.name, health = self.health, maxhealth = self.maxhealth))
            return True

    def crit(self):
        # If the random generated number is lower than the minions critchance then he lands a crit strike on the player.
        if (random()*100 < self.critchance * 5):
            print("\n{minion} lands a critical strike!\n".format(minion = self.name))
            return 2
        return 1

    def attack_hero(self, hero):
        # Call the hero.dodge() method to check if the hero dodges the attack. If he does dodge will be set to True if not it will be set to False.
        dodge = hero.dodge()
        if dodge:
            # If the player dodged the attack inform him about it.
            print("You dodged {enemy}'s attack!\n".format(enemy = self.name))
            return True
        else:
            # If the player did not dodge continue with the damage calculation
            # if the crit method returns 2 it means is a critical strike and damage will be doubled. if not it will return 1.
            crit = self.crit()
            return (hero.lose_health(round((self.maxhealth * 0.75 + self.attack) - (hero.maxhealth * 0.5 + hero.defense))*crit))

# The spawnminion function will create minions for the player to fight against as the player progresses the enemies will be stronger.
def spawnminion(attack, defense, speed, critchance, maxhealth, lvl):
    # Depending of the lvl of the minion to be created we:
    # - Select the monster name if it's not a boss from the minion list. for the bosses we have set fixed names.
    # - Lower the stats of the monster for the minions so that the player is stronger than them.
    # - This changes with the bosses.
    #   - The first boss will be 95% as strong as the player.
    #   - The second boss will be as strong as the player.
    #   - The third boss will be 5% stronger than the player.
    #   - The last boss will be 10% stronger than the player.
    # Also if the player has not trained enough (Doesn't have a set level against each boss then the bosses advantage will be even greater and in some cases virtually imposible to defeat until the player gets to that level.)
    # This is calculated on the boss() function.
    # Once this is defined a Minion object is created with the stats calculated to fight against the Hero.
    match lvl:
        case 1:
            index = randint(0,6)
            lower_stats = randint(75,80)
            percentage_lower_stats = lower_stats/100
            return Minion(minion_list[index], round(attack*percentage_lower_stats), round(defense*percentage_lower_stats), round(speed * percentage_lower_stats), round(critchance * percentage_lower_stats), round(maxhealth * percentage_lower_stats))
        case 2:
            index = randint(7,13)
            lower_stats = randint(80,85)
            percentage_lower_stats = lower_stats/100
            return Minion(minion_list[index], round(attack*percentage_lower_stats), round(defense*percentage_lower_stats), round(speed * percentage_lower_stats), round(critchance * percentage_lower_stats), round(maxhealth * percentage_lower_stats))
        case 3:
            index = randint(14,20)
            lower_stats = randint(85,90)
            percentage_lower_stats = lower_stats/100
            return Minion(minion_list[index], round(attack*percentage_lower_stats), round(defense*percentage_lower_stats), round(speed * percentage_lower_stats), round(critchance * percentage_lower_stats), round(maxhealth * percentage_lower_stats))
        case 4:
            percentage_lower_stats = 95/100
            return Minion('Abadon', round(attack*percentage_lower_stats), round(defense*percentage_lower_stats), round(speed * percentage_lower_stats), round(critchance * percentage_lower_stats), round(maxhealth * percentage_lower_stats))
        case 5:
            percentage_lower_stats = 1
            return Minion('Mammon', round(attack*percentage_lower_stats), round(defense*percentage_lower_stats), round(speed * percentage_lower_stats), round(critchance * percentage_lower_stats), round(maxhealth * percentage_lower_stats))
        case 6:
            percentage_lower_stats = 105/100
            return Minion('Belphegor', round(attack*percentage_lower_stats), round(defense*percentage_lower_stats), round(speed * percentage_lower_stats), round(critchance * percentage_lower_stats), round(maxhealth * percentage_lower_stats))
        case 7:
            percentage_lower_stats = 110/100
            return Minion('Lucifer', round(attack*percentage_lower_stats), round(defense*percentage_lower_stats), round(speed * percentage_lower_stats), round(critchance * percentage_lower_stats), round(maxhealth * percentage_lower_stats))