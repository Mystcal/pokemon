"""
TITLE: POKEMON BASE Task 1
GROUP: T06G05
AUTHOR: MAH YUNG JIAN 31921582 
EDITS: LAU ZI FU 32637888

Description:
Allows the creation of a pokemon team to be used for battle. The players will get to choose their number of pokemon and their player name 
to generate a pokemon team. The order of the pokemon in the team is determined by the battle mode.
"""

from tokenize import Pointfloat
from pokemon import Charmander, Bulbasaur, MissingNo, Squirtle, MissingNo
from queue_adt import CircularQueue
from stack_adt import ArrayStack
from array_sorted_list import ArraySortedList
from sorted_list import ListItem

class PokeTeam:

    limit = 6   #constant class variable
    missingNo_limit = 1

    def __init__(self, name: str) -> None:
        
        #instance variables
        self.name = name 
        self.battle_mode = None
        self.team = None
        self.team_copy = []

    def team_limit(self, Charmander: int, Bulbasaur: int, Squirtle: int, MissingNo: int) -> bool:   
        """check if number of pokemon exceeds limit"""
        if (Charmander + Bulbasaur + Squirtle + MissingNo) <= (PokeTeam.limit):
            return True       
        return False

    def assign_team(self, charm: int, bulb:int, squir: int, Miss: int) -> None:
        """ Assigns teams based on number of pokemon and battlemode. Is intended to use within the choose_team function.\n
        battlemode 0 = ArrayStack \n
        battlemode 1 = CircularQueue\n
        battlemode 2 = ArraySortedList

        :pre: total of number of pokemon <= 6\n
        :raises Exeception: if the total number of pokemon exceeds 6\n
        :complexity: best/worst case is O(N), N is length of ADT used
        """
        if not self.team_limit(charm, bulb, squir, Miss):
            raise ValueError("Cannot Exceed limit")
        else:
            if self.battle_mode == 0: #when battlemode is 0
                self.team = ArrayStack(PokeTeam.limit)

                if Miss == 1:
                    self.team.push(MissingNo()) #missingNo will always be last

                for i in range(squir):
                    self.team.push(Squirtle())

                for i in range(bulb):
                    self.team.push(Bulbasaur())

                for i in range(charm):
                    self.team.push(Charmander())

            elif self.battle_mode == 1: #when battlemode is 1
                
                self.team = CircularQueue(PokeTeam.limit)

                for i in range(charm):
                    self.team.append(Charmander())
                
                for i in range(bulb):
                    self.team.append(Bulbasaur())

                for i in range(squir):
                    self.team.append(Squirtle())
                
                if Miss == 1:
                    self.team.append(MissingNo()) #missingNo will always be last

            elif self.battle_mode == 2: #when battlemode is 2
                self.team = ArraySortedList(PokeTeam.limit)
                # choose key attribute
                # populate using key:pokemon
                # insert in non-ascending order
                #if Miss == 1:
                    #self.team.add_descending(MissingNo())

                if (self.criterion == 'hp'):

                    if Miss == 1:
                        m = MissingNo()
                        self.team.add(ListItem(m, 0))
                    for i in range(charm):
                        c = Charmander()
                        self.team.add(ListItem(c, c.get_hp()))
                    for i in range(bulb):
                        b = Bulbasaur()
                        self.team.add(ListItem(b, b.get_hp()))
                    for i in range(squir):
                        s = Squirtle()
                        self.team.add(ListItem(s, s.get_hp()))
                    
                    
                elif (self.criterion == 'lvl'):
                    if Miss == 1:
                        m = MissingNo()
                        self.team.add(ListItem(m, 0))
                    for i in range(charm):
                        c = Charmander()
                        self.team.add(ListItem(c, c.get_level()))
                    for i in range(bulb):
                        b = Bulbasaur()
                        self.team.add(ListItem(b, b.get_level()))
                    for i in range(squir):
                        s = Squirtle()
                        self.team.add(ListItem(s, s.get_level()))
                    

                elif (self.criterion == 'attack'):
                    if Miss == 1:
                        m = MissingNo()
                        self.team.add(ListItem(m, 0))

                    for i in range(charm):
                        c = Charmander()
                        self.team.add(ListItem(c, c.get_attack()))
                    for i in range(bulb):
                        b = Bulbasaur()
                        self.team.add(ListItem(b, b.get_attack()))
                    for i in range(squir):
                        s = Squirtle()
                        self.team.add(ListItem(s, s.get_attack()))

                elif (self.criterion == 'defence'):
                    if Miss == 1:
                        m = MissingNo()
                        self.team.add(ListItem(m, 0))

                    for i in range(charm):
                        c = Charmander()
                        self.team.add(ListItem(c, c.get_defence()))
                    for i in range(bulb):
                        b = Bulbasaur()
                        self.team.add(ListItem(b, b.get_defence()))
                    for i in range(squir):
                        s = Squirtle()
                        self.team.add(ListItem(s, s.get_defence()))

                elif (self.criterion == 'speed'):
                    if Miss == 1:
                        m = MissingNo()
                        self.team.add(ListItem(m, 0))
                    for i in range(charm):
                        c = Charmander()
                        self.team.add(ListItem(c, c.get_speed()))
                    for i in range(bulb):
                        b = Bulbasaur()
                        self.team.add(ListItem(b, b.get_speed()))
                    for i in range(squir):
                        s = Squirtle()
                        self.team.add(ListItem(s, s.get_speed()))




    def choose_team(self, battle_mode: int, criterion: str = None) -> None:
        """ Prompts the user to choose the numbers of pokemon and subsequently create the team based on the battle_mode.\n
        :pre: battle_mode must be either 0, 1, or 2 and user input must be in the form of C B S M. Example: 2 2 2\n
        :raises Exception: if battle_mode is not in [0, 1, 2] or user input not in the form of C B S M\n
        :complexity: best case O(N), N is length of ADT used. Worst case O(M), M is the number of invalid input from user
        """
        while battle_mode in [0, 1, 2]: #will keep looping until user enters the correct amount of pokemon
            self.battle_mode = battle_mode
            self.criterion = criterion
            self.team_copy = []
            print("Howdy Trainer! Choose your team as C B S M or C B S (Without MissingNo)")
            print("Where C is the number of Charmanders \n\tB is the number of Bulbasaurs \n\tS is the number of Squirtles \n\tM is the number of MissingNo (not more than one )")
            i = input("").split(" ") #When user doesn't choose MissingNo

            for item in i: #check if input is a number
                a = item.isnumeric()
                if a == False:
                    break

            if not a: 
                print("Input should only be number\n")
                continue
            
            #if input is 3
            elif len(i) == 3:           
                char = int(i[0])
                bulb = int(i[1])
                squir = int(i[2])
                miss = 0

            #if input is 4
            elif len(i) == 4: #When user chooses MissingNo
                char = int(i[0])
                bulb = int(i[1])
                squir = int(i[2])
                miss = int(i[3])

            else:
                print("not a valid input, should be in the form of C B S or C B S M specifically.")
                continue
            
            if self.team_limit(char, bulb, squir, miss) and miss <= PokeTeam.missingNo_limit:
                #to be used later in __str__ function
                [self.team_copy.append(Charmander()) for i in range(char)]
                [self.team_copy.append(Bulbasaur()) for i in range(bulb)]
                [self.team_copy.append(Squirtle()) for i in range(squir)]
                [self.team_copy.append(MissingNo()) for i in range(miss)]
                #assigns teams based on battlemode
                self.assign_team(char, bulb, squir, miss) 
                return None

            #print more specific errors
            elif miss > PokeTeam.missingNo_limit and self.team_limit(char, bulb, squir, miss):
                print("MissingNo cannot be more than 1 in a team\n")
                continue
            else:
                print("Cannot Exceed limit\n")
                continue

        raise ValueError("Battle mode should be 0, 1 or 2\n")

    def get_team(self): 
        """ returns the ADT object containing the pokemon team"""
        return self.team

    def get_name(self) -> str:
        """ returns the player name of the team"""
        return self.name

    def __str__(self) -> str:
        """ returns the description of a PokeTeam object in string format \n
        :complexity: best/worst case O(N) where N is the number of elements in the ADT data structures.
        """

        #returns string based on battle_mode
        if self.battle_mode == None:
            if len(self.team_copy) == 0: #returns nothing if team is empty
                return ""
            
            # converts list to string 
            res = str(self.team_copy[0]) 

            for i in range(1, len(self.team_copy)):
                res += ", " + str(self.team_copy[i])
        
        #returns string using ArrayStack ADT implementation
        elif self.battle_mode == 0:
            copy = [] #copy to python list to print out
            for i in range(len(self.team)): 
                item = self.team.pop()
                copy.append(item)
            for i in copy:
                self.team.push(i) 

            if len(copy) == 0: #returns nothing if team is empty
                return ""
            
            # converts list to string 
            res = str(copy[0]) 

            for i in range(1, len(copy)):
                res += ", " + str(copy[i])

            return res
            
        #returns string using CircularQueue ADT implementation
        elif self.battle_mode == 1:
            copy = [] #copy to python list to print out
            for i in range(len(self.team)):
                item = self.team.serve()
                copy.append(item)
                self.team.append(item)

            if len(copy) == 0: #returns nothing if team is empty
                return ""
            
            # converts list to string 
            res = str(copy[0]) 

            for i in range(1, len(copy)):
                res += ", " + str(copy[i])

            return res

        #returns string using ArraySortedList implementation
        elif self.battle_mode == 2:
            copy = [] #copy to python list to print out
            self.team.reverse()

            while len(self.team) > 0:
                item = self.team.delete_at_index(0)
                copy.append(item)
            
            for item in copy:
                self.team.add(item)

            if len(copy) == 0: #returns nothing if team is empty
                return ""

            # converts list to string 
 
            res = str(copy[0].value)

            for i in range(1, len(copy)):

                res += ", " + str(copy[i].value)

            return res
