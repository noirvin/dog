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
        self.deaths = 0
        self.kills = 0
        # values passed in


    def attack(self):
      ''' Return a value between 0 and the value set by self.max_damage.'''
      # TODO: Use random.randint(a, b) to select a random attack value.
      random_attack_value = random.randint( 0 , self.max_damage )
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

        return random.randint(0 , self.max_block)


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
              print(self.name + " won!")


          else:

              opponent.add_deaths()
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

            print("Hero Name: "+hero.name)
            print("kills: "+hero.kills)
            print("deaths: "+hero.deaths)












if __name__ == "__main__":

    # If you run this file from the terminal
    # this block of code is executed.
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
