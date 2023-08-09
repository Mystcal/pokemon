"""
TITLE: POKEMON Task 1
GROUP: T06G05
AUTHOR: MAH YUNG JIAN 31921582 
EDITS: LIM YU JIN 32637888, LAU ZI FU 32685092

Description:
The implementaion of PokemonBase ADT and GlitchMon ADT (which itself is also a children class of PokemonBase).
There are a total of 3 types of pokemon classes that are the direct implementations of PokemonBase ADT, with one execption 
being MissingNo, as it is the direct child class of GlitchMon
"""

import random
from pokemon_base import GlitchMon, PokemonBase        #child class of PokemonBase

class Charmander(PokemonBase):

    #Class Variables
    class_effectiveness = {"Fire": 1, "Water": 0.5, "Grass": 2, "Neutral": 1 } #Effectiveness against other pokemon types
    base_hp = 7
    base_attack = 6
    base_defence = 4
    base_speed = 7

    def __init__(self) -> None:

        PokemonBase.__init__(self, Charmander.base_hp, "Fire")   #hp and type
        self.name = "Charmander" 
        self.attack = Charmander.base_attack + 1
        self.defence = Charmander.base_defence 
        self.speed = Charmander.base_speed + 1
    
    def get_name(self) -> str:
        """ returns the pokemon name """     # it gets the pokemon name from the class name
        return self.name                      # returns the pokemon name


    def get_attack(self) -> int:
        """ returns the current attack value of the pokemon """  
        return self.attack     #returns attack


    def get_defence(self) -> int:
        """ returns the current defence value of the pokemon """
        return self.defence     #returns defence

    def get_speed(self) -> int:
        """ returns the current speed value of the pokemon """ 
        return self.speed  # returns speed

    def set_level(self, new_level: int) -> None:
        """ sets the current level to new level"""
        self.level = new_level
        self.attack = Charmander.base_attack + self.get_level()
        self.speed = Charmander.base_speed + self.get_level()

    def level_up(self) -> None:
        """ increases current pokemon level by one"""
        self.level += 1
        self.speed = Charmander.base_speed + self.get_level()
        self.attack = Charmander.base_attack + self.get_level()

    def damage_done(self, damage: int) -> None:
        """ calculates damage when defending. damage is from the attacking pokemon.
        :pre: damage must be > 0
        :raises Exeception: damage is more than 0
        :complexity: best/worst case O(1)
        """

        PokemonBase.damage_done(self, damage)  #takes precond the damage done method from PokemonBase class
        self.damage = damage  #creating local variable of damage

        #damage being done to Charmander
        if self.damage > self.get_defence():
            self.hp = self.get_hp() - self.damage  #setting new hp after being damanged
        else:
            self.hp = self.get_hp() - self.damage // 2    ##setting new hp after being damanged


class Bulbasaur(PokemonBase):

    #Class Variables
    class_effectiveness = {"Fire": 0.5, "Water": 2, "Grass": 1, "Neutral": 1 } #Effectiveness against other pokemon types
    base_hp = 9
    base_attack = 5
    base_defence = 5
    base_speed = 7


    def __init__(self) -> None:

        PokemonBase.__init__(self, Bulbasaur.base_hp, "Grass")   #hp and type
        self.name = "Bulbasaur"
        self.attack = Bulbasaur.base_attack
        self.defence = Bulbasaur.base_defence 
        self.speed = int(Bulbasaur.base_speed + 1//2)


    def get_name(self) -> str:
        """returns the pokemon name"""  # it gets the pokemon name from the class name
        return self.name                     # returns the pokemon name

    def get_attack(self) -> int:
        """ returns the current attack value of the pokemon """
        return self.attack     #returns attack


    def get_defence(self) -> int:
        """ returns the current defence value of the pokemon """
        return self.defence     #returns defence


    def get_speed(self) -> int:
        """ returns the current speed value of the pokemon """
        return self.speed  # returns speed

    def set_level(self, new_level: int) -> None:
        """ sets the current level to new level"""
        self.level = new_level
        self.speed = Charmander.base_speed + self.get_level()//2

    def level_up(self) -> None:
        """ increases current pokemon level by one"""
        self.level += 1
        self.speed = Charmander.base_speed + self.get_level()//2

    def damage_done(self, damage: int) -> None:  # calculates damage after being attacked
        """ calculates damage when defending. damage is from the attacking pokemon.
        :pre: damage must be > 0
        :raises Exeception: damage is more than 0
        :complexity: best/worst case O(1)
        """

        PokemonBase.damage_done(self, damage)  #takes precond the damage done method from PokemonBase class
        self.damage = damage  #creating local variable of damage

        #damage being done to Charmander
        if self.damage > self.get_defence() + 5:
            self.hp = self.hp - self.damage     #setting new hp after being damanged
        else:
            self.hp = self.hp - self.damage // 2    ##setting new hp after being damanged


class Squirtle(PokemonBase):

    #Class Variables
    class_effectiveness = {"Fire": 2, "Water": 1, "Grass": 0.5, "Neutral": 1 } #Effectiveness against other pokemon types
    base_hp = 8
    base_attack = 4
    base_defence = 6
    base_speed = 7


    def __init__(self) -> None:

        PokemonBase.__init__(self, Squirtle.base_hp, "Water")   #hp and type
        self.name = "Squirtle"  
        self.attack = int(Squirtle.base_attack + 1//2)
        self.defence = Squirtle.base_defence + 1
        self.speed = Squirtle.base_speed


    def get_name(self) -> str:
        """returns the pokemon name"""      # it gets the pokemon name from the class name
        return self.name                     # returns the pokemon name

    def get_attack(self) -> int:
        """ returns the current attack value of the pokemon """
        return self.attack  # returns attack

    def get_defence(self) -> int:
        """ returns the current defence value of the pokemon """
        return self.defence     #returns defence

    def get_speed(self) -> int:
        """ returns the current speed value of the pokemon """   
        return self.speed  # returns speed

    def set_level(self, new_level: int) -> None:
        """ sets the current level to new level"""
        self.level = new_level
        self.attack = Squirtle.base_attack + self.get_level()//2
        self.defence = Squirtle.base_defence + self.get_level()

    def level_up(self) -> None:
        """ increases current pokemon level by one"""
        self.level += 1
        self.attack = Squirtle.base_attack + self.get_level()//2
        self.defence = Squirtle.base_defence + self.get_level()

    def damage_done(self, damage: int) -> None:  # calculates damage after being attacked
        """ calculates damage when defending. damage is from the attacking pokemon.
        :pre: damage must be > 0
        :raises Exeception: damage is more than 0
        :complexity: best/worst case O(1)
        """

        PokemonBase.damage_done(self, damage)  #takes precond the damage done method from PokemonBase class
        self.damage = damage  #creating local variable of damage

        #damage being done to Charmander
        if self.damage > self.get_defence() * 2:
            self.hp = self.hp - self.damage     #setting new hp after being damanged
        else:
            self.hp = self.hp - self.damage // 2    ##setting new hp after being damanged


############# FOR TASK 6 MISSINGNO ####################################################################################################
class MissingNo(GlitchMon):
    class_effectiveness = {"Fire": 1, "Water": 1, "Grass": 1, "Neutral": 1} #Effectiveness against other pokemon types
    base_hp = int((Charmander.base_hp + Bulbasaur.base_hp + Squirtle.base_hp)/3)
    base_attack = ((Charmander.base_attack + 1) + Bulbasaur.base_attack + (Squirtle.base_attack + 1//2)) // 3 
    base_defence = (Charmander.base_defence + Bulbasaur.base_defence + (Squirtle.base_defence + 1)) // 3 
    base_speed = ((Charmander.base_speed + 1) + (Bulbasaur.base_speed + 1//2) + Squirtle.base_speed) // 3 

    def __init__(self) -> None:

        PokemonBase.__init__(self, MissingNo.base_hp, "Neutral")   #hp and type
        self.name = "MissingNo"
        self.attack = MissingNo.base_attack + 1
        self.defence = MissingNo.base_defence + 1
        self.speed = MissingNo.base_speed + 1


    def get_name(self) -> str:
        """returns the pokemon name"""   # it gets the pokemon name from the class name
        return self.name                     # returns the pokemon name

    def get_hp(self) -> int:
        """ returns the current hp of the pokemon object """
        return self.hp

    def get_attack(self) -> int:
        """ returns the current attack value of the pokemon """
        return self.attack  # returns attack

    def get_defence(self) -> int:
        """ returns the current defence value of the pokemon """
        return self.defence     #returns defence


    def get_speed(self) -> int:
        """ returns the current speed value of the pokemon """
        return self.speed  # returns speed

    def set_level(self, new_level: int) -> None:
        """ sets the current level to new level"""
        self.level = new_level
        self.hp = PokemonBase.get_hp(self) + self.get_level() - 1
        self.attack = MissingNo.base_attack + self.get_level()
        self.speed = MissingNo.base_defence + self.get_level()  
        self.defence = Squirtle.base_speed + self.get_level()

    def level_up(self) -> None:
        """ increases current pokemon level by one"""
        self.level += 1
        self.hp = PokemonBase.get_hp(self) + self.get_level() - 1
        self.attack = MissingNo.base_attack + self.get_level()
        self.speed = MissingNo.base_defence + self.get_level()  
        self.defence = Squirtle.base_speed + self.get_level()


    def damage_done(self, damage: int) -> None:  # calculates damage after being attacked
        """ calculates damage when defending. damage is from the attacking pokemon.
        :pre: damage must be > 0
        :raises Exeception: damage is more than 0
        :complexity: best/worst case O(1)
        """

        GlitchMon.damage_done(self, damage)  #takes precond the damage done method from PokemonBase class
        self.damage = damage  #creating local variable of damage

        i = [0,1,2,3]
        dmg_taken_type = random.choice(i)

        if dmg_taken_type == 0:
            if self.damage > self.get_defence():
                self.hp = self.get_hp() - self.damage  #setting new hp after being damanged
            else:
                self.hp = self.get_hp() - self.damage // 2    ##setting new hp after being damanged
        
        elif dmg_taken_type == 1:
            if self.damage > self.get_defence() + 5:
                self.hp = self.hp - self.damage     #setting new hp after being damanged
            else:
                self.hp = self.hp - self.damage // 2    ##setting new hp after being damanged
    
        elif dmg_taken_type == 2:
            if self.damage > self.get_defence() * 2:
                self.hp = self.hp - self.damage     #setting new hp after being damanged
            else:
                self.hp = self.hp - self.damage // 2    ##setting new hp after being damanged
        
        elif dmg_taken_type == 3:
            self.superpower()

