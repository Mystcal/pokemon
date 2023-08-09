"""
TITLE: battle 
TASK 3: SET MODE BATTLE
TASK 4: ROTATING MODE BATTLE
TASK 5: OPTIMIZED MODE BATTLE

GROUP: T06G05
AUTHOR: LIM YU JIN 32637888 (Task 3), 
        LAU ZI FU 32685092 (Task 4),
        Low Lup Hoong 31167934 (Task 5)


Description:
Allows two players to play a pokemon game with different battle modes.
The battlemodes are: SET MODE BATTLE, ROTATING MODE BATTLE, OPTIMIZED MODE BATTLE. In order to play a game, the user will have to 
create an instance of the class "Battle" and then call the specific battle mode functions to play the battlemodes.

"""

from re import T
from pokemon import Charmander, MissingNo, Squirtle, Bulbasaur
from poke_team import PokeTeam
from stack_adt import ArrayStack
from typing import Union
from sorted_list import ListItem

class Battle:
    
    def __init__(self, trainer_one_name: str, trainer_two_name: str) -> int:

        self.team1 = PokeTeam(trainer_one_name)
        self.team2 = PokeTeam(trainer_two_name)

        self.battle_mode = None

    def attack_order(self, p1: Union[Charmander,Squirtle,Bulbasaur,MissingNo], p2: Union[Charmander,Squirtle,Bulbasaur,MissingNo]) -> None:
        """Calculates damage dealt and attack order. Returns 2 pokemon, 1st is attacking, second is defending.
        :pre: input must be objects of either Charmander, Squirtle, Bulbasaur or MissingNo class
        :raise Exception: when input is not the correct type
        :complexity: O(1)
        test in test_rotating_mode_battle
        """

        check = isinstance(p1, (Charmander, Squirtle, Bulbasaur, MissingNo)) and isinstance(p2, (Charmander, Squirtle, Bulbasaur, MissingNo))

        if not check:
            raise TypeError("input must be objects of type Charmander, Squirtle, Bulbasaur, MissingNo")

        #p1 is the attacker
        if p1.get_speed() > p2.get_speed():
            damage = p1.get_attack() * type(p1).class_effectiveness[p2.get_poke_type()]
            p2.damage_done(damage)

            if not p2.fainted():
                damage = p2.get_attack() * type(p2).class_effectiveness[p1.get_poke_type()]
                p1.damage_done(damage) 

        #p1 and p2 defend and attack simultaneously

        elif p1.get_speed() == p2.get_speed():
            damage = p1.get_attack() * type(p1).class_effectiveness[p2.get_poke_type()]
            p2.damage_done(damage)

            damage = p2.get_attack() * type(p2).class_effectiveness[p1.get_poke_type()]
            p1.damage_done(damage)

        #p2 is the attacker
        else:
            damage = p2.get_attack() * type(p2).class_effectiveness[p1.get_poke_type()]
            p1.damage_done(damage)

            if not p1.fainted():
                damage = p1.get_attack() * type(p1).class_effectiveness[p2.get_poke_type()]
                p2.damage_done(damage)  

    def assign_key(self, poke: ListItem, criterion: str) -> None:
        """ Updates the key of the ListItem object.
        :pre: criteria in ["hp", "lvl", 'speed', "attack", "defence"]
        :raise exception: criteria not in ["hp", "lvl", 'speed', "attack", "defence"]
        :complexity: best/worst case O(1)
        used in task 5
        """
        if criterion not in ["hp", "lvl", 'speed', "attack", "defence"]:
            raise ValueError(" criterion should be in ['hp', 'lvl', 'speed', 'attack', 'defence']")
        else:
            if criterion == "hp":
                poke.key = int(poke.value.get_hp())

            elif criterion == "lvl":
                poke.key = int(poke.value.get_level())

            elif criterion == "speed":
                poke.key = int(poke.value.get_speed())

            elif criterion == "attack":
                poke.key = int(poke.value.get_attack())

            elif criterion == "defence":
                poke.key = int(poke.value.get_defence())


############################    TASK 3    #######################################################################################################



    def set_mode_battle(self) -> int:
        """Pop the pokemon from both team and conduct the battle the pokemon will higher speed will attack first
        if both the pokemon have the same speed both will attack at the same time
        at the end of each attack if both pokemon are not fainted then both the pokemon hp will be deducted by 1
        at the end of each attack if pokemon is not fainted it will be push back to its team stack
        at the end of each attack if the opponent pokemon is fainted then the friendly pokemon will level up
        the battle ends when either of the team is empty
        :pre: Team1 and Team2 is not empty.
        :raise Execption:  if user input not in the form of C B S
        Best Case : O(1), when the defending team has 1 pokemon and faints instantly
        Worst Case : O(n) , n is the total number of attacks from both teams"""
        
        #set battle_mode to 0
        battle_mode = 0
        self.battle_mode = battle_mode

        #player 1 choose their pokemons
        print('Team 1 assigned: ' + str(self.team1.get_name()))
        self.team1.choose_team(self.battle_mode)
         
        #player 2 choose their pokemons    
        print('Team 2 assigned: ' + str(self.team2.get_name()))       
        self.team2.choose_team(self.battle_mode)
        
        #show the team coordination
        print('Team 1: ' + str(self.team1))
        print('Team 2: ' + str(self.team2))
        
        #reverse the stack(pokemon team)           
        team_1 = ArrayStack(len(self.team1.team))
        team_2 = ArrayStack(len(self.team2.team))
        for i in range(len(self.team1.team)):
            team_1.push(self.team1.team.pop())
        for i in range(len(self.team2.team)):
            team_2.push(self.team2.team.pop())

        i = 1
            
        #if there are pokemons alive in each team,
        while not team_1.is_empty() and not team_2.is_empty():
            
            #Pop pokemon from each team as representative for their team for the round
            poke_1 = team_1.pop()
            poke_2 = team_2.pop()  

            #while both of the representative pokemons are not fainted
            while not poke_1.fainted() and not poke_2.fainted():

                self.attack_order(poke_1, poke_2)

                #if both pokemon not fainted decrease the hp by 1
                if not poke_1.fainted() and not poke_2.fainted():
                    poke_1.set_hp(poke_1.get_hp() - 1) 
                    poke_2.set_hp(poke_2.get_hp() - 1)
                    
                    #if team1's pokemon is fainted and team2's pokemon is not fainted, team2's pokemon level up and push back to the stack
                    if poke_1.fainted() and not poke_2.fainted():
                        poke_2.level_up()
                        team_2.push(poke_2)                        
                        break

                    #if team2's pokemon is fainted and team1's pokemon is not fainted, team1's pokemon level up and push back to the stack
                    elif poke_2.fainted() and not poke_1.fainted():
                        poke_1.level_up()
                        team_1.push(poke_1)
                        break
                    #if both of the representative pokemon is not fainted, they will be push back to their team
                    elif not poke_1.fainted() and not poke_2.fainted():
                        team_1.push(poke_1)
                        team_2.push(poke_2)
                        break

                #Level up pokemon after defeating the other
                #if team1's pokemon is fainted and team2's pokemon is not fainted, team2's pokemon level up and push back to the stack
                elif poke_1.fainted() and not poke_2.fainted():
                    poke_2.level_up()
                    team_2.push(poke_2)
                    break
                
                #if team2's pokemon is fainted and team1's pokemon is not fainted, team1's pokemon level up and push back to the stack
                elif poke_2.fainted() and not poke_1.fainted():
                    poke_1.level_up()
                    team_1.push(poke_1)
                    break 
            
            #news for every round
            if not poke_1.fainted() and poke_2.fainted():
                print("Round {}: Team 1's {} faints Team 2's {}".format(i, poke_1.get_name(), poke_2.get_name()))
            
            elif not poke_2.fainted() and poke_1.fainted():
                print("Round {}: Team 1's {} is fainted by Team 2's {}".format(i, poke_1.get_name(), poke_2.get_name()))

            elif poke_1.fainted() and poke_2.fainted():
                print("Round {}: Team 1's {} and Team2's {} fight at each other and both faints".format(i, poke_1.get_name(), poke_2.get_name()))
            
            else:
                print("Round {}: Team 1's {} and Team2's {} fight at each other and no one faints".format(i, poke_1.get_name(), poke_2.get_name()))

            i += 1

        #if both team have no more pokemon then return draw
        if team_1.is_empty() and team_2.is_empty():
            return "Draw"
        
        #return winner
        #if team 1 has no more pokemon and team 2 is not empty, return the team2's player name 
        elif team_1.is_empty() and not team_2.is_empty():
            return self.team2.get_name()
            
        #if team 2 has no more pokemon and team 1 is not empty, return the team1's player name
        elif team_2.is_empty() and not team_1.is_empty():
            return self.team1.get_name()


############################    TASK 4    #######################################################################################################

    def rotating_mode_battle(self) -> str:
        """In this mode, a Pokemon fights a round, and then is sent to the back of the team, making the next pokemon in the party fight the next
        round. The battle ends when at least one of the teams is empty. For this battle mode, the CircularQueue implementation of Queue ADT will
        be used.
        :pre: Team1 and Team2 is not empty.
        :raise Execption:  if user input not in the form of C B S
        Best Case : O(1), when the defending team has 1 pokemon and faints instantly
        Worst Case : O(n) , n is the total number of attacks from both teams
        """
        
        self.battle_mode = 1

        #Asks users for input to Assemble team1 and team2
        print("\nTeam1: {}".format(self.team1.get_name()))
        self.team1.choose_team(self.battle_mode)

        print("\nTeam2: {}".format(self.team2.get_name()))
        self.team2.choose_team(self.battle_mode)

        #assigns t1 and t2 to the team of each player


        print('team1:' + str(self.team1))
        print('team1:' + str(self.team2))

        t1 = self.team1.get_team()
        t2 = self.team2.get_team()

        i = 1
        while not t1.is_empty() and not t2.is_empty(): #will keep looping until either team1 or team2 loses

            p1 = t1.serve()
            p2 = t2.serve()

            #Calculates damage dealt and attack order
            self.attack_order(p1, p2)

            #Calculate hp status of Attacking and Defending pokemon
            
            if p1.fainted() and not p2.fainted(): 
                #if team1's pokemon is fainted and team2's pokemon is not fainted, team2's pokemon level up append back to queue
                p2.level_up()
                t2.append(p2)
                print("Round {}: team2's {} faints team1's {}".format(i, p2.get_name(), p1.get_name()))

            
            elif not p1.fainted() and p2.fainted():
                #if team2's pokemon is fainted and team1's pokemon is not fainted, team1's pokemon level up append back to queue
                p1.level_up()
                t1.append(p1)
                print("Round {}: team1's {} faints team2's {}".format(i, p1.get_name(), p2.get_name()))

            elif not p1.fainted() and not p2.fainted(): 
                #both pokemon will lose 1 hp if both are alive after initial attacks
                p1.set_hp(p1.get_hp() - 1) 
                p2.set_hp(p2.get_hp() - 1)


                if p1.fainted() and not p2.fainted():
                    #if team1's pokemon is fainted and team2's pokemon is not fainted, team2's pokemon level up append back to queue
                    p2.level_up()
                    t2.append(p2)
                    print("Round {}: team2's {} faints team1's {}".format(i, p2.get_name(), p1.get_name()))

                elif not p1.fainted() and p2.fainted():
                    #if team2's pokemon is fainted and team1's pokemon is not fainted, team1's pokemon level up append back to queue
                    p1.level_up()
                    t1.append(p1)
                    print("Round {}: team1's {} faints team2's {}".format(i, p1.get_name(), p2.get_name()))
                
                elif not p1.fainted() and not p2.fainted():
                    #if both are alive, append both back to their respective team's queues
                    t1.append(p1)
                    t2.append(p2)
                    print("Round {}: team1's {} and team2's {} fight at the same time and both is alive".format(i, p1.get_name(), p2.get_name()))
                
                elif p1.fainted() and p2.fainted():
                    #both faints nothing happens
                    print("Round {}: team1's {} and team2's {} fight at the same time and both faints".format(i, p1.get_name(), p2.get_name()))
                
            elif p1.fainted() and p2.fainted():
                #both faints nothing happens
                print("Round {}: team1's {} and team2's {} fight at the same time and both faints".format(i, p1.get_name(), p2.get_name()))

            i += 1

        # returns winner
        if t1.is_empty() and not t2.is_empty(): #if winner is team2
            return self.team2.get_name()
        
        elif t2.is_empty() and not t1.is_empty(): #if winner is team1
            return self.team1.get_name()

        else:
            return "Draw" #if both teams lose

############################    TASK 5    #######################################################################################################

    def optimised_mode_battle(self, criterion_team1: str, criterion_team2: str) -> str:
        """In this mode, the pokemon are grouped based on the selected criteria, and will continue to be sorted based on criteria during the battle.
        :pre: Team1 and Team2 is not empty.
        :raise Execption:  if user input not in the form of C B S, or criterion_team1 and criterion_team2 is not in ['hp', 'lvl', 'attack', 'defence', 'speed']
        Best Case : O(1), when the defending team has 1 pokemon and faints instantly
        Worst Case : O(n) , n is the total number of attacks from both teams
        """
        self.battle_mode = 2

        if criterion_team1.lower() not in ['hp', 'lvl', 'attack', 'defence', 'speed'] and criterion_team2.lower() not in ['hp', 'lvl', 'attack', 'defence', 'speed']:
            raise Exception("Inputted critera should be 'hp', 'lvl', 'attack', 'defence', or  'speed'" )

        # asks the user for input and sets up the players’ teams in such an order
        # Asks users for input to Assemble team1 and team2
        # team1_key_attribute = input("Chosen Attribute: ").lower()
        print("\nTeam1: {}".format(self.team1.get_name()))
        print("Chosen Attribute: {}".format(criterion_team1))
        self.team1.choose_team(self.battle_mode, criterion_team1.lower())


        print("\nTeam2: {}".format(self.team2.get_name()))
        print("Chosen Attribute: {}".format(criterion_team2))
        self.team2.choose_team(self.battle_mode, criterion_team2.lower())

        #assigns t1 and t2 to the team of each player
        team_1 = self.team1.get_team()
        print('team1:' + str(self.team1))
        team_2 = self.team2.get_team()
        print('team2:' + str(self.team2))

        # where the Pokemon come in the battle in non-increasing order of the chosen attribute by the user

        i = 1
        # if there are pokemons alive in each team,
        while len(team_1) != 0 and len(team_2) != 0:

            # remove pokemon from front most index at 0 to battle
            poke_1 = team_1.delete_at_index(len(team_1) - 1)
            poke_2 = team_2.delete_at_index(len(team_2) - 1)

            # while both of the representative pokemons are not fainted

            # deal damage
            self.attack_order(poke_1.value, poke_2.value)

            #if both pokemons faints, leave carcass and move one
            if poke_1.value.fainted() and poke_2.value.fainted():
                 break

            # if both pokemon not fainted decrease the hp by 1,
            elif not poke_1.value.fainted() and not poke_2.value.fainted():
                poke_1.value.set_hp(poke_1.value.get_hp() - 1 )
                poke_2.value.set_hp(poke_2.value.get_hp() - 1 )

                #if both still, alive, send back to team
                if not poke_1.value.fainted() and not poke_2.value.fainted():
                    # both sent back to team
                    self.assign_key(poke_1, criterion_team1)
                    team_1.add(poke_1)
                    self.assign_key(poke_2, criterion_team2)
                    team_2.add(poke_2)

                # if after -1hp, poke 1 alive, poke 1 lvl up and sent back
                elif not poke_1.value.fainted() and poke_2.value.fainted():
                    poke_1.value.level_up()
                    self.assign_key(poke_1, criterion_team1)
                    team_1.add(poke_1)

                # if after -1hp, poke 2 alive, poke 2 lvl up and sent back
                elif poke_1.value.fainted() and not poke_2.value.fainted():
                    poke_2.value.level_up()
                    self.assign_key(poke_2, criterion_team2)
                    team_2.add(poke_2)

                elif poke_1.value.fainted() and poke_2.value.fainted():
                    break

            # if one of the poke faints after attack
            elif  poke_1.value.fainted() and not poke_2.value.fainted():
                poke_2.value.level_up()
                self.assign_key(poke_2, criterion_team2)
                team_2.add(poke_2)

            else: # not poke_1.fainted() and  poke_2.fainted():
                poke_1.value.level_up()
                self.assign_key(poke_1, criterion_team1)
                team_1.add(poke_1)

            # Print Result for each round
            if not poke_1.value.fainted() and poke_2.value.fainted():
                print("Round {}: Team 1's {} faints Team 2's {}".format(i, poke_1.value.get_name(), poke_2.value.get_name()))

            elif poke_1.value.fainted() and  not poke_2.value.fainted():
                print("Round {}: Team 2's {} faints Team 1's {}".format(i, poke_2.value.get_name(), poke_1.value.get_name()))

            elif poke_1.value.fainted() and poke_2.value.fainted():
                print("Round {}: Team 1's {} and Team2's {} fight at each other and both faints".format(i,
                poke_1.value.get_name(),
                poke_2.value.get_name()))

            else:
                print("Round {}: Team 1's {} and Team2's {} fight at each other and no one faints".format(i,
                poke_1.value.get_name(),
                poke_2.value.get_name()))


            i += 1

        # if both team have no more pokemon then return draw
        if team_1.is_empty() and team_2.is_empty():
            return "Draw"

        # return winner
        # if team 1 has no more pokemon and team 2 is not empty, return the team2's player name
        elif team_1.is_empty() and not team_2.is_empty():
            return self.team2.get_name()

        # if team 2 has no more pokemon and team 1 is not empty, return the team1's player name
        elif team_2.is_empty() and not team_1.is_empty():
            return self.team1.get_name()




x = Battle('x','y')
x.rotating_mode_battle()