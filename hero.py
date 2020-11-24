from ability import Ability
from armor import Armor
from weapon import Weapon
import random

class Hero:
    # We want our hero to have a default "starting_health"
    def __init__(self, name, starting_health = 100):
        '''Instance properties:
            abilities: List
            armors: List
            name: String
            starting_health: Integer
            current_health: Integer
        '''
        # Abilities and armors don't have starting values and are set to empty lists on initialization
        self.abilities = list()
        self.armors = list()
        # We know the name of our hero, so we assign it here
        self.name = name
        # Similarly, our starting health is passed in, just like name
        self.starting_health = starting_health
        # When a hero is created, their current health is
        # always the same as their starting health (no damage taken yet!)
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0


    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        # We use the append method to add ability objects to our list.
        self.abilities.append(ability)

    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        # This method will append the weapon object passed in as an argument to self.abilities.
        # This means that self.abilities will be a list of abilities and weapons.
        self.abilities.append(weapon)

    def attack(self):
        '''Calculate the total damage from all ability attacks.
            return: total_damage:Int
        '''
        # Start our total out at 0
        total_damage = 0
        # Loop through all of our hero's abilities
        for ability in self.abilities:
            # Add the damage of each attack to our running total
            total_damage += int(ability.attack())
        # Return the total damage
        return total_damage

    def add_armor(self, armor):
        '''Add armor to self.armors
            Armor: Armor Object
        '''
        # We use the append method to add armor objects to our list.
        self.armors.append(armor)

    def add_kill(self, num_kills):
        ''' Update self.kills by num_kills amount'''
        # Add the number of kills to self.kills
        self.kills += num_kills

    def defend(self, damage_amt):
        '''Calculate the incoming damage minus the total block amount from all armor blocks.
            return: damage_amt - total_block:Int
        '''
        # Start our block total out at 0
        total_block = 0
        # Loop through all of our hero's armors (but first check if there are any)
        if self.armors:
            for armor in self.armors:
                # Add the block damage of each armor to our running total
                total_block += armor.block()
        # Return the block total subtracted from incoming damage
        return damage_amt - total_block

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.
        '''
        # Updates self.current_health to the current
        # minus the the amount returned from calling self.defend(damage).
        self.current_health -= self.defend(damage)

    def add_death(self, num_deaths):
        ''' Update deaths with num_deaths'''
        # Add the number of deaths to self.deaths
        self.deaths += num_deaths

    def is_alive(self):  
        '''Return True or False depending on whether the hero is alive or not.
        '''
        # Check the current_health of the hero.
        # If it is <= 0, then return False. Otherwise, they still have health
        # and are therefore alive, so return True
        if self.current_health <= 0:
            return False
        else:
            return True


    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.
        '''
        # First version: Randomly choose winner by picking from a list of the hero and the opponent
        # winner = random.choice([self, opponent])
        # print(f"{winner.name} won!")

        # Fight each hero until a victor emerges.
        # Check if at least one hero has abilities. If no hero has abilities, print "Draw"
        if not self.abilities and not opponent.abilities:
            print("Draw")
        # Else, start the fighting loop until a hero has won
        else:
            fight_loop = True
            while fight_loop:
                # The hero (self) and their opponent must attack each other and each must take damage from the other's attack
                # After each attack, check if either the hero (self) or the opponent is alive
                # If one of them has died, print "{HeroName} won!", and end the fight loop
                opponent.take_damage(self.attack())
                if opponent.is_alive() == False:
                    winner = self
                    # Update the number of kills the hero (self) has when the opponent dies.
                    self.add_kill(1)
                    # Update the number of deaths of the opponent if they die in the fight
                    opponent.add_death(1)
                    fight_loop = False
                self.take_damage(opponent.attack())
                if self.is_alive() == False:
                    winner = opponent
                    # Update the number of kills the opponent has when the hero (self) dies
                    opponent.add_kill(1)
                    # Update the number of deaths of the hero (self) if they die in the fight
                    self.add_death(1)
                    fight_loop = False
            print(f"{winner.name} won!")
            return winner



# ----------------------------------------------------------------------------
# TESTS
# ----------------------------------------------------------------------------

# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block is executed.
#     my_hero = Hero("Grace Hopper", 200)
#     print(my_hero.name)
#     print(my_hero.current_health)

# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block is executed.
#     ability = Ability("Great Debugging", 50)
#     hero = Hero("Grace Hopper", 200)
#     hero.add_ability(ability)
#     ability2 = Ability("Better Debugging", 100)
#     hero.add_ability(ability2)
#     print(hero.abilities)

# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block of code is executed.
#     ability = Ability("Great Debugging", 50)
#     another_ability = Ability("Smarty Pants", 90)
#     hero = Hero("Grace Hopper", 200)
#     hero.add_ability(ability)
#     hero.add_ability(another_ability)
#     print(hero.attack())

# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block of code is executed.

#     hero = Hero("Grace Hopper", 200)
#     shield = Armor("Shield", 50)
#     hero.add_armor(shield)
#     hero.take_damage(50)
#     print(hero.current_health)

# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block is executed.

#     hero = Hero("Grace Hopper", 200)
#     hero.take_damage(150)
#     print(hero.is_alive())
#     hero.take_damage(15000)
#     print(hero.is_alive())

# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block is executed.

#     hero1 = Hero("Wonder Woman")
#     hero2 = Hero("Dumbledore")
#     ability1 = Ability("Super Speed", 300)
#     ability2 = Ability("Super Eyes", 130)
#     ability3 = Ability("Wizard Wand", 180)
#     ability4 = Ability("Wizard Beard", 220)
#     hero1.add_ability(ability1)
#     hero1.add_ability(ability2)
#     hero2.add_ability(ability3)
#     hero2.add_ability(ability4)
#     hero1.fight(hero2)

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())