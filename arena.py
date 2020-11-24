from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
    def __init__(self, name1, name2):
        '''Instantiate properties
            team_one: None
            team_two: None
        '''
        # Create instance variables named team_one and team_two that will hold our teams.
        self.team_one = Team(name1)
        self.team_two = Team(name2)

    def create_ability(self):
        '''Prompt for Ability information.
            return Ability with values from user Input
        '''
        # Lets a user create an ability by inputting name and max damage of ability
        name = input("What is the ability name?  ")
        max_damage = int(input(
            "What is the max damage of the ability?  "))
        return Ability(name, max_damage)

    def create_weapon(self):
        '''Prompt user for Weapon information
            return Weapon with values from user input.
        '''
        # This method will allow a user to create a weapon.
        # Prompt the user for the necessary information to create a new weapon object.
        # return the new weapon object.
        name = input("What is the weapon name?  ")
        max_damage = int(input(
            "What is the max damage of the weapon?  "))
        return Weapon(name, max_damage)

    def create_armor(self):
        '''Prompt user for Armor information
          return Armor with values from user input.
        '''
        # This method will allow a user to create a piece of armor.
        #  Prompt the user for the necessary information to create a new armor object.
        #  return the new armor object with values set by user.
        name = input("What is the armor name?  ")
        max_block = int(input(
            "What is the max damage that the armor can block?  "))
        return Armor(name, max_block)

    def create_hero(self):
        '''Prompt user for Hero information
          return Hero with values from user input.
        '''
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
           add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
           if add_item == "1":
               # Add an ability to the hero
               new_ability = self.create_ability()
               hero.add_ability(new_ability)
           elif add_item == "2":
               # Add a weapon to the hero
               new_weapon = self.create_weapon()
               hero.add_weapon(new_weapon)
           elif add_item == "3":
               # Add an armor to the hero
               new_armor = self.create_armor()
               hero.add_armor(new_armor)
        return hero

    def build_team_one(self):
        '''Prompt the user to build team_one '''
        # This method should allow a user to create team one.
        # Prompt the user for the number of Heroes on team one
        # call self.create_hero() for every hero that the user wants to add to team one.
        # Add the created hero to team one.
        numOfTeamMembers = int(input("How many members would you like on Team One?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        '''Prompt the user to build team_two'''
        # This method should allow a user to create team two.
        # Prompt the user for the number of Heroes on team two
        # call self.create_hero() for every hero that the user wants to add to team two.
        # Add the created hero to team two.
        numOfTeamMembers = int(input("How many members would you like on Team Two?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        '''Battle team_one and team_two together.'''
        # This method should battle the teams together.
        # Call the attack method that exists in your team objects for battle functionality.
        self.team_one.attack(self.team_two)

    def average_kd(self, team):
        '''Calculates average Kill/Death ratio for a team'''
        # For each team, calculate the total kills and deaths for each hero,
        # find the average kills and deaths by dividing the totals by the number of heroes.
        # finally, divide the average number of kills by the average number of deaths for each team
        team_kills = 0
        team_deaths = 0
        # Add up all collective kills and deaths for a team
        for hero in team.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        # Prevent division by zero by replacing 0 in denominator with 1
        if team_deaths == 0:
            team_deaths = 1
        return(team.name + " average K/D: " + str(team_kills / team_deaths))

    def survivors_and_winning_team(self):
        '''List surviving heroes on each team and declare the winning team'''
        team_one_survivors = 0
        team_two_survivors = 0
        # For each team, loop through all of their heroes,
        # and use the .deaths property to check for alive heroes,
        # printing their names and increasing the survival count if they're alive.
        for hero in self.team_one.heroes:
            if hero.deaths == 0:
                team_one_survivors += 1
                print("Survived from " + self.team_one.name + ": " + hero.name)
        for hero in self.team_two.heroes:
            if hero.deaths == 0:
                team_two_survivors += 1
                print("Survived from " + self.team_two.name + ": " + hero.name)
        # Based off of the count of alive heroes, the winning team
        # is declared by whichever team has more alive heroes
        if team_one_survivors > team_two_survivors:
            return(f"{self.team_one} won!")
        elif team_two_survivors > team_one_survivors:
            return(f"{self.team_two} won!")
        else:
            return("It's a tie!")
    
    def show_stats(self):
        '''Prints team statistics to terminal.'''
        # This method should print out battle statistics
        # including each team's average kill/death ratio.
        # Required Stats:
        #     Show surviving heroes.
        #     Declare winning team
        #     Show both teams' average kill/death ratio
        print("\n")
        print(self.team_one.name + " statistics: ")
        self.team_one.stats()
        print("\n")
        print(self.team_two.name + " statistics: ")
        self.team_two.stats()
        print("\n")

        # Calculate the average K/D ratio for Team One and Team Two
        print(self.average_kd(self.team_one))
        print(self.average_kd(self.team_two))

        # Print the survivors on each team and declare the winning team
        print(self.survivors_and_winning_team())


# Game Loop

if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena("Team One", "Team Two")

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()

# ----------------------------------------------------------------------------
# TESTS
# ----------------------------------------------------------------------------

# if __name__ == "__main__":
#     arena = Arena("Team One", "Team Two")
#     arena.build_team_one()
#     arena.build_team_two()
#     arena.team_battle()
#     arena.show_stats()