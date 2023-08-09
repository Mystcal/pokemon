"""

Description:
Pokemon ADT to be implemented
Also Contains GlitchMon ADT
The file contains all the required and abstract functions a future Pokemon Child Class needs.
"""

from abc import ABC, abstractmethod
import random



class PokemonBase:              #the initial level for all pokemon is 1. The child classes will contain all the same methods.


    initial_level = 1
    def __init__(self, hp: int, poke_type: str) -> None:

        if hp < 0:
            raise ValueError("hp should be >= 0")
        self.hp = hp

        if poke_type not in ["Fire", "Water", "Grass", "Neutral"]:
            raise TypeError("poke_type must be one of [\"Fire\", \"Water\", \"Grass\", \"Neutral\"]")
        self.poke_type = poke_type
        self.level = self.initial_level


    def get_hp(self) -> int:
        """ returns the current hp of the pokemon object 
        O(1)"""
        return self.hp

    def set_hp(self, new_hp: int) -> None:
        """ sets the current hp to a new value """
        self.hp = new_hp

    def get_level(self) -> int:
        """ returns the current level of the pokemon """
        return self.level


    def fainted(self) -> bool:  #to see whether pokemon fainted after battle
        """ True if the hp of a pokemon is <= 0"""
        return self.hp <= 0

    def get_poke_type(self) -> str:
        """ returns the type of the pokemon. The type is either one of ['Fire', 'Water', 'Grass', 'Neutral']"""
        return self.poke_type

    @abstractmethod
    def set_level(self, new_level: int) -> None:
        """ sets the current level to new level"""
        pass

    @abstractmethod
    def level_up(self) -> None:
        """ increases current pokemon level by one"""
        pass


    @abstractmethod
    def get_name(self) -> str:
        """ returns the pokemon name """
        pass

    @abstractmethod
    def get_speed(self) -> int:
        """ returns the current speed value of the pokemon """
        pass

    @abstractmethod
    def get_attack(self) -> int:
        """ returns the current attack value of the pokemon """
        pass

    @abstractmethod
    def get_defence(self) -> int:
        """ returns the current defence value of the pokemon """
        pass

    @abstractmethod
    def damage_done(self, damage: int) -> None:    #calculates damage after being attacked
        """ calculates damage when defending. damage is from the attacking pokemon.
        :pre: damage must be > 0
        :raises Exeception: damage is more than 0
        """
        if damage < 0:
            raise ValueError("damage done must be >=0")
        pass

    def __str__(self):                      #returns formatted string
        return "{}'s HP = {} and level = {}".format(self.get_name(), self.get_hp(), self.get_level())


class GlitchMon(PokemonBase):
    
    def increase_hp(self) -> None:
        """ increases MissingNo hp by one"""
        self.hp += 1

    def superpower(self) -> None:
        """ Increases hp or level of MissingNo based on chance """
        i = [0,1,2]
        power = random.choice(i)

        if power == 0:
            self.level_up()

        elif power == 1:
            self.increase_hp()
        
        elif power == 2:
            self.increase_hp()
            self.level_up()



