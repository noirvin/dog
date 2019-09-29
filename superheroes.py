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

        return random.randint( 0 , self.max_block )


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

              print(self.name + " won!")

          else:

              print(opponent.name + " won!")
      else:

          print("Draw!!")








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
