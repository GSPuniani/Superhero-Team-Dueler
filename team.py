from hero import Hero
import random

class Team:
    def __init__(self, name):
        ''' Initialize your team with its team name and an empty list of heroes
        '''
        self.name = name
        self.heroes = list()

    def remove_hero(self, name):
        '''Remove hero from heroes list.
        If Hero isn't found return 0.
        '''
        foundHero = False
        # Loop through each hero in our list
        for hero in self.heroes:
            # If we find them, remove them from the list
            if hero.name == name:
                self.heroes.remove(hero)
                # Set our indicator to True
                foundHero = True
        # If we looped through our list and did not find our hero,
        # the indicator would have never changed, so return 0
        if not foundHero:
            return 0

    def view_all_heroes(self):
        '''Prints out all heroes to the console.'''
        # Loop over the list of heroes and print their names to the terminal one by one.
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        '''Add Hero object to self.heroes.'''
        # Add the Hero object that is passed in to the list of heroes in self.heroes
        self.heroes.append(hero)

    def stats(self):
        '''Print team statistics'''
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print("{} Kill/Deaths: {}".format(hero.name, kd))

    def revive_heroes(self, health=100):
        ''' Reset all heroes health to starting_health'''
        # For each hero in self.heroes,
        # set the hero's current_health to their starting_health
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def attack(self, other_team):
        ''' Battle each team against each other.'''

        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents) > 0:
            # 1) Randomly select a living hero from each team 
            random_hero = random.choice(living_heroes)
            random_opponent = random.choice(living_opponents)
            # 2) Have the heroes fight each other: .fight() returns the winner
            # 3) update the list of living_heroes and living_opponents
            # to reflect the result of the fight
            if random_hero.fight(random_opponent) == random_hero:
                living_opponents.remove(random_opponent)
            elif random_hero.fight(random_opponent) == random_opponent:
                living_heroes.remove(random_hero)
            