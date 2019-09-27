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

if __name__ == "__main__":

    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())
