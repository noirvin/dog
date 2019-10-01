import random

class Ability:
    def __init__(self, name, max_damage):
        '''Create Instance Variables:
          name:String
          max_damage: Integer
          '''
        # TODO: Instantiate the variables listed in the docstring with then
        self.name = name
        self.max_damage = max_damage

        # values passed in


    def attack(self):
      ''' Return a value between 0 and the value set by self.max_damage.'''
      # TODO: Use random.randint(a, b) to select a random attack value.
      random_attack_value = random.randint( 0 , int(self.max_damage) )
      # Return an attack value between 0 and the full attack.
      # Hint: The constructor initializes the maximum attack value.
      return random_attack_value


class Armor:
    def __init__(self, name, max_block):
        '''Instantiate instance properties.
            name: String
            max_block: Integer
        '''
        # TODO: Create instance variables for the values passed in.
        self.name = name
        self.max_block = max_block

    def block(self):
        ''' Return a random value between 0 and the initialized max_block strength. '''

        return random.randint(0 , int(self.max_block))


class Hero:
    def __init__(self, name, starting_health=100):
        '''Instance properties:
          abilities: List
          armors: List
          name: String
          starting_health: Integer
          current_health: Integer
        '''
        # TODO: Initialize instance variables values as instance variables
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0
        # (Some of these values are passed in above,
        # others will need to be set at a starting value)
        # abilities and armors are lists that will contain objects that we can use

    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        # TODO: Add ability object to abilities:List
        self.abilities.append(ability)

    def attack(self):
        '''Calculate the total damage from all ability attacks.
        return: total:Int
        '''
        # TODO: This method should run Ability.attack() on every ability
        sum = 0
        for ability in self.abilities:

            # in self.abilities and returns the total as an integer.

            sum += Ability.attack(ability)
        return sum


    def add_armor(self, armor):
      '''Add armor to self.armors
        Armor: Armor Object
      '''
      # TODO: Add armor object that is passed in to `self.armors`
      for armor in self.armors:

          self.armors.append(armor)


    def defend(self, damage_amt):
      '''Runs `block` method on each armor.
          Returns the damage amount minus the sum of all blocks
      '''
      # TODO: This method should run the block method on each armor in self.armors
      sum = 0
      for armor in self.armors:

         sum += armor.block()


      return damage_amt - sum


    def take_damage(self, damage_amt):
      '''Updates self.current_health to reflect the damage minus the defense.
      '''
      # TODO: Create a method that updates self.current_health to the current
      # minus the the amount returned from calling self.defend(damage).
      self.current_health = self.current_health - self.defend(damage_amt)



    def is_alive(self):
      '''Return True or False depending on whether the hero is alive or not.
      '''
      # TODO: Check whether the hero is alive and return true or false
      if self.current_health < 1:
         return False
      else:
         return True

    def fight(self, opponent):
      ''' Current Hero will take turns fighting the opponent hero passed in.
      '''
      # TODO: Fight each hero until a victor emerges.
      if len(self.abilities) > 0 or len(opponent.abilities) > 0:
          while(self.is_alive() and opponent.is_alive()):

              opponent.take_damage(self.attack())

              self.take_damage(opponent.attack())

          # Print the victor's name to the screen.
          if self.is_alive():

              self.add_kill(1)
              opponent.add_deaths(1)
              print(self.name + " won!")


          else:

              opponent.add_kill(1)
              self.add_deaths(1)
              print(opponent.name + " won!")
      else:

          print("Draw!!")
    #TODO: Refactor this method to update the
        # number of kills the hero has when the opponent dies.
        # Also update the number of deaths for whoever dies in the fight

    def add_kill(self, num_kills):
        ''' Update kills with num_kills'''
        # TODO: This method should add the number of kills to self.kills
        self.kills += num_kills

    def add_deaths(self, num_deaths):
        ''' Update deaths with num_deaths'''
        # TODO: This method should add the number of deaths to self.deaths
        self.deaths += num_deaths

    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        # TODO: This method will append the weapon object passed in as an
        # argument to self.abilities.
        # This means that self.abilities will be a list of
        # abilities and weapons.
        self.abilities.append(weapon)

    def add_armor(self, armor):
        '''Add Armor to self.armors
            armor: Armor Object
        '''
        # TODO: This method will add the armor object that is passed in to
        # the list of armor objects defined in the constructor: `self.armors`.
        self.armors.append(armor)


class Weapon(Ability):

    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        # TODO: Use what you learned to complete this method.
        half_amount = self.max_damage//2
        return random.randint(half_amount, int(self.max_damage))



class Team:
    def __init__(self, name):
        ''' Initialize your team with its team name
        '''
        # TODO: Implement this constructor by assigning the name and heroes, which should be an empty list
        self.name = name
        self.heroes = []

    def remove_hero(self, name):
        '''Remove hero from heroes list.
        If Hero isn't found return 0.
        '''
        # TODO: Implement this method to remove the hero from the list given their name.
        name_in_list = False
        for hero in self.heroes:

                if hero.name == name:

                    name_in_list = True
                    self.heroes.remove(hero)

        if name_in_list == False:

            return 0


    def view_all_heroes(self):
        '''Prints out all heroes to the console.'''
        # TODO: Loop over the list of heroes and print their names to the terminal.
        for hero in self.heroes:

            print(hero.name)

    def add_hero(self, hero):
      '''Add Hero object to self.heroes.'''
      # TODO: Add the Hero object that is passed in to the list of heroes in
      # self.heroes
      self.heroes.append(hero)

    def attack(self, other_team):
        ''' Battle each team against each other.'''
        # TODO: Randomly select a living hero from each team and have
        # them fight until one or both teams have no surviving heroes.
        # Hint: Use the fight method in the Hero class.
        alive_members = []
        alive_members_2 = []

        for hero in self.heroes:

            if hero.is_alive():

                alive_members.append(hero)

        for hero_2 in other_team.heroes:

            if hero.is_alive():

                alive_members_2.append(hero_2)

        while (len(alive_members) > 0 and len(alive_members_2) > 0):

            Hero_one = random.choice(alive_members)
            Hero_two = random.choice(alive_members_2)

            Hero_one.fight(Hero_two)

            if Hero_one.is_alive() == False:

                alive_members.remove(Hero_one)

            else:

                alive_members_2.remove(Hero_two)


    def revive_heroes(self, health=100):
        ''' Reset all heroes health to starting_health'''
        # TODO: This method should reset all heroes health to their
        # original starting value.
        for hero in self.heroes:

            hero.current_health = health


    def stats(self):
        '''Print team statistics'''
        # TODO: This method should print the ratio of kills/deaths for each
        # member of the team to the screen.
        # This data must be output to the console.
        # Hint: Use the information stored in each hero.
        for hero in self.heroes:

            print(self.name + "stats: ")
            print("Hero Name: " + hero.name)
            print("kills: " + str(hero.kills))
            print("deaths: " + str(hero.deaths))


class Arena:
    def __init__(self):
        '''Instantiate properties
            team_one: None
            team_two: None
        '''
        self.team_one = None
        self.team_two = None

    def create_ability(self):
        '''Prompt for Ability information.
            return Ability with values from user Input
        '''
        # TODO: This method will allow a user to create an ability.
        # Prompt the user for the necessary information to create a new ability object.
        # return the new ability object.
        name = input("Type an ability you want to add: ")
        max_damage = input("Type a number from 1 to 100 for the maximum damage of this ability: ")
        ability = Ability(name, max_damage)
        return ability

    def create_weapon(self):
        '''Prompt user for Weapon information
            return Weapon with values from user input.
        '''
        # TODO: This method will allow a user to create a weapon.
        # Prompt the user for the necessary information to create a new weapon object.
        # return the new weapon object.

        name = input("Type a weapon you want to add: ")
        max_damage = input("Type a number from 1 to 80 for the maximum damage of this weapon: ")
        weapon = Weapon(name, max_damage)
        return weapon

    def create_armor(self):
        '''Prompt user for Armor information
          return Armor with values from user input.
        '''
        # TODO:This method will allow a user to create a piece of armor.
        #  Prompt the user for the necessary information to create a new armor
        #  object.
        #
        #  return the new armor object with values set by user.
        name = input("Type an armor you want to add: ")
        max_block = input("Type a number from 1 to 100 for the maximum amount of block: ")

        armor = Armor(name, max_block)
        return armor

    def create_hero(self):
        '''Prompt user for Hero information
          return Hero with values from user input.
        '''
        # TODO: This method should allow a user to create a hero.
        # User should be able to specify if they want armors, weapons, and
        # abilities.
        # Call the methods you made above and use the return values to build
        # your hero.
        #
        # return the new hero object
        name = input("Type a name for the hero you want to add: ")

        hero = Hero(name)

        ability_decision = input("Would you like to add an ability for your character? y/n? ")

        while ability_decision != "y" and ability_decision != "n":

            print("wrong letter!!")
            ability_decision = input("Enter a letter again: ")

        if ability_decision == "y":

            hero.add_ability(self.create_ability())

        weapon_decision = input("Would you like to add a weapon for your hero? y/n? ")

        while weapon_decision != "y" and weapon_decision != "n":

            print("wrong letter!!")
            weapon_decision = input("Enter a letter again: ")

        if weapon_decision == "y":

            hero.add_weapon(self.create_weapon())

        armor_decision = input("Would you like to add armor for your hero? ")

        while armor_decision != "y" and armor_decision != "n":

            print("wrong letter!!")
            armor_decision = input("Enter a letter again: ")

        if armor_decision == "y":

            hero.add_armor(self.create_armor())

        return hero

    def build_team_one(self):
        '''Prompt the user to build team_one '''
        # TODO: This method should allow a user to create team one.
        # Prompt the user for the number of Heroes on team one
        # call self.create_hero() for every hero that the user wants to add to team one.
        #
        # Add the created hero to team one.
        num_of_heroes = input("Enter a number from 3 to 20 for the number of heroes you want in team 1: ")
        name = input("choose a name for team 1: ")
        self.team_one = Team(name)

        for i in range(int(num_of_heroes)):

            hero = self.create_hero()
            self.team_one.heroes.append(hero)

    def build_team_two(self):
        '''Prompt the user to build team_two'''
        # TODO: This method should allow a user to create team two.
        # Prompt the user for the number of Heroes on team two
        # call self.create_hero() for every hero that the user wants to add to team two.
        #
        # Add the created hero to team two.
        num_of_heroes = input("Enter a number from 3 to 20 for the number of heroes you want in team 2: ")
        name = input("choose a name for team 2: ")
        self.team_two = Team(name)

        for i in range(int(num_of_heroes)):

            hero = self.create_hero()
            self.team_two.heroes.append(hero)

    def team_battle(self):
        '''Battle team_one and team_two together.'''
        # TODO: This method should battle the teams together.
        # Call the attack method that exists in your team objects
        # for that battle functionality.

        self.team_one.attack(self.team_two)

    def show_stats(self):
        '''Prints team statistics to terminal.'''
        # TODO: This method should print out battle statistics
        # including each team's average kill/death ratio.
        # Required Stats:
        #     Declare winning team
        #     Show both teams average kill/death ratio.
        #     Show surviving heroes.

        survivors_one = []
        survivors_two = []

        for hero in self.team_one.heroes:

            if hero.is_alive():

                survivors_one.append(hero)

        for hero in self.team_two.heroes:

            if hero.is_alive():

                survivors_two.append(hero)

        if len(survivors_one)>len(survivors_two):

            print(self.team_one.name + " has won!")

        elif len(survivors_one) == len(survivors_two):

            print("It's a draw!")

        else:

            print(self.team_two.name + " has won!")

        print(self.team_one.stats())
        print(self.team_two.stats())

        print("surviving heroes of " + self.team_one.name)
        for hero in self.team_one.heroes:
            if hero.is_alive():

                print(hero.name)

        print("surviving heroes of " + self.team_two.name)
        for hero in self.team_two.heroes:
            if hero.is_alive():

                print(hero.name)








if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

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
