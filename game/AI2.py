from agent import Agent
import random

class AI_Agent2(Agent):        
    '''A sample implementation of a random agent in the game The Resistance'''

    def __init__(self, name='Rando'):
        '''
        Initialises the agent.
        Nothing to do here.
        '''
        self.name = name

    def new_game(self, number_of_players, player_number, spy_list):
        '''
        initialises the game, informing the agent of the 
        number_of_players, the player_number (an id number for the agent in the game),
        and a list of agent indexes which are the spies, if the agent is a spy, or empty otherwise
        '''
        self.number_of_players = number_of_players
        self.player_number = player_number
        self.spy_list = spy_list
        self.rounds_complete = 0
        self.missions_failed = 0

        #self.suspicion is an array of size number_of_players to show the chances of them being spy, 
        #everyone starts at 0, number goes up if theyre more suspicious and down if they are less.
        self.suspicion = {}
        for i in range(number_of_players):
            self.suspicion[i] = 0

        if number_of_players == 5 or number_of_players == 6:
            self.number_of_spies = 2
        elif number_of_players == 7 or  number_of_players == 8 or number_of_players == 9:
            self.number_of_spies = 3
        elif number_of_players == 10:
            self.number_of_spies = 4
        

    def is_spy(self):
        '''
        returns True iff the agent is a spy
        '''
        return self.player_number in self.spy_list

    def propose_mission(self, team_size, betrayals_required = 1):
        '''
        expects a team_size list of distinct agents with id between 0 (inclusive) and number_of_players (exclusive)
        to be returned. 
        betrayals_required are the number of betrayals required for the mission to fail.
        '''
        team = []

        #decisions if the agent is a spy
        if self.is_spy():
            key_list = list(self.suspicion.keys())
            val_list = list(self.suspicion.values())
            sorted_list = val_list.copy()
            sorted_list.sort()

            #get as many spies as possible if the mission is critical
            if self.critical_mission():
                for i in range(self.number_of_players):
                    smallest = sorted_list[i]
                    position = val_list.index(smallest)
                    if len(team) == team_size:
                        if key_list[position] in self.spy_list:
                            team.append(key_list[position])
                    else:
                        break

            #put the least suspicious spy in the mission
            for i in range(self.number_of_players):
                smallest = sorted_list[i]
                position = val_list.index(smallest)
                if key_list[position] in self.spy_list:
                    team.append(key_list[position])
                    break

            #put the least suspicious res in the misison
            for i in range(self.number_of_players):
                smallest = sorted_list[i]
                position = val_list.index(smallest)
                if key_list[position] not in team:
                    team.append(key_list[position])
                    break




        #If the agent is not a spy, put the least suspicious players on the team
        else:
           
            key_list = list(self.suspicion.keys())
            val_list = list(self.suspicion.values())
            sorted_list = val_list.copy()
            sorted_list.sort()

            for i in range(team_size):
                smallest = sorted_list[i]
                position = val_list.index(smallest)
                team.append(key_list[position])



        return team    

    def vote(self, mission, proposer):
        '''
        mission is a list of agents to be sent on a mission. 
        The agents on the mission are distinct and indexed between 0 and number_of_players.
        proposer is an int between 0 and number_of_players and is the index of the player who proposed the mission.
        The function should return True if the vote is for the mission, and False if the vote is against the mission.
        '''
        vote = False

        #vote for our own proposals
        if proposer == self.player_number:
            return True


        #a list of all players sorted with the most suspicous 1st
        key_list = list(self.suspicion.keys())
        val_list = list(self.suspicion.values())
        sorted_list = val_list.copy()
        sorted_list.sort(reverse=True)

        #finds the most suspicous
        position = val_list.index(sorted_list[0])
        most_suspicious = key_list[position]

        #the most suspicious, same lengths as number of spies
        potential_spies = []
        for i in range(self.number_of_spies):
            position = val_list.index(sorted_list[0])
            potential_spies.append(key_list[position])

        #Logic is we are the spy
        if self.is_spy():

            #is there a spy on this mission?
            spy_on_mission = False
            for i in mission:
                if i in self.spy_list:
                    spy_on_mission = True

            #on critical missions, we need a spy on the team to win
            if self.critical_mission():
                if(spy_on_mission):
                    return True

            
            #acting like a res, only voting for missions with the least suspicious
            for i in mission:
                if i in potential_spies:
                    return False

            #if nothings else happens, vote yes if there is a spy on the team
            return spy_on_mission


        #Logic is we are not the spy
        else:

            #if a potential spy is on the mission or proposed the mission,
            #vote is False
            for i in potential_spies:
                if i in mission:
                    return False
                if i == proposer:
                    return False




            #gets a rating for how dangerous the mission could be
            mission_suspicion = 0
            for i in mission:
                mission_suspicion += self.suspicion[i]
            avg_mission_suspicion = mission_suspicion / len(mission)

            #gets a rating for how dangerous the group is
            total_suspicion = 0
            for i in self.suspicion:
                total_suspicion += self.suspicion[i]
            avg_suspicion = total_suspicion / len(self.suspicion)
            
            #if the mission is more dangerous than the group average, dont do the mission
            if(avg_mission_suspicion > avg_suspicion):
                return False

            #if the mission proposer is more dangerous than the group average, dont do the mission
            if(self.suspicion[proposer] > avg_suspicion):
                return False

        #All saftey checks done, and mission is deemed safe
        return True
    def vote_outcome(self, mission, proposer, votes):
        '''
        mission is a list of agents to be sent on a mission. 
        The agents on the mission are distinct and indexed between 0 and number_of_players.
        proposer is an int between 0 and number_of_players and is the index of the player who proposed the mission.
        votes is a dictionary mapping player indexes to Booleans (True if they voted for the mission, False otherwise).
        No return value is required or expected.
        '''

        mission_sus = False

        key_list = list(self.suspicion.keys())
        val_list = list(self.suspicion.values())
        sorted_list = val_list.copy()
        sorted_list.sort(reverse=True)

        #the most suspicious players, same lengths as number of spies
        potential_spies = []
        for i in range(self.number_of_spies):
            position = val_list.index(sorted_list[0])
            potential_spies.append(key_list[position])

        for i in mission:
            if i in potential_spies:
                mission_sus = True

        #if the mission is suspicious, everyone related to the mission is a little more suspicious
        if(mission_sus):
            for i in mission:
                self.suspicion[i] += 5
            self.suspicion[proposer] += 5

            for i in votes:
                self.suspicion[i] += 5
            
    def betray(self, mission, proposer):
        '''
        mission is a list of agents to be sent on a mission. 
        The agents on the mission are distinct and indexed between 0 and number_of_players, and include this agent.
        proposer is an int between 0 and number_of_players and is the index of the player who proposed the mission.
        The method should return True if this agent chooses to betray the mission, and False otherwise. 
        By default, spies will betray 30% of the time. 
        '''
        
        #betray is it is critical
        if self.critical_mission():
            return True

        #do not betray if all the spies are on the mission
        if self.spy_list in mission:
            #return False
            return False
        
        #gets a rating for how dangerous the group is
        total_suspicion = 0
        for i in self.suspicion:
            total_suspicion += self.suspicion[i]
        avg_suspicion = total_suspicion / len(self.suspicion)

        #if i have below average suspicion
        if self.suspicion[self.player_number] <= avg_suspicion:
            return True

        teammates = []
        for i in mission:
            if i != self.player_number:
                teammates.append(i)

        mission_suspicion = 0
        for i in teammates:
            mission_suspicion += self.suspicion[i]
        if mission_suspicion != 0:
            avg_mission_suspicion = mission_suspicion / len(teammates)
        else:
            avg_mission_suspicion = 0
        #if i have below average team suspicion
        if self.suspicion[self.player_number] <= avg_mission_suspicion:
            return True

        #80% chance to betray if its suspicious (need points to win c:)
        return (random.randint(1,10) < 9)


    def mission_outcome(self, mission, proposer, betrayals, mission_success):
        '''
        mission is a list of agents to be sent on a mission. 
        The agents on the mission are distinct and indexed between 0 and number_of_players.
        proposer is an int between 0 and number_of_players and is the index of the player who proposed the mission.
        betrayals is the number of people on the mission who betrayed the mission, 
        and mission_success is True if there were not enough betrayals to cause the mission to fail, False otherwise.
        It iss not expected or required for this function to return anything.
        '''

        if mission_success:
            for i in mission:
                self.suspicion[i] -= 20
            self.suspicion[proposer] -= 20


        else:

            #if everyone on the mission betrays, then they are all spies
            if betrayals == len(mission):
                for i in mission:
                    self.suspicion[i] += 100

            sus_modifier = float(betrayals)/float(len(mission))
            for i in mission:
                self.suspicion[i] += 100*sus_modifier
            self.suspicion[proposer] += 40*sus_modifier
                
            

    def round_outcome(self, rounds_complete, missions_failed):
        '''
        basic informative function, where the parameters indicate:
        rounds_complete, the number of rounds (0-5) that have been completed
        missions_failed, the numbe of missions (0-3) that have failed.
        '''
        self.rounds_complete = rounds_complete
        self.missions_failed = missions_failed
        pass
    
    def game_outcome(self, spies_win, spies):
        '''
        basic informative function, where the parameters indicate:
        spies_win, True iff the spies caused 3+ missions to fail
        spies, a list of the player indexes for the spies.
        '''
        #nothing to do here
        
        if self.is_spy() and spies_win:
            f = open("agent_results2.txt", "a")
            f.write(" SPY-WIN")
            f.close()
        elif self.is_spy() and not spies_win:
            f = open("agent_results2.txt", "a")
            f.write(" SPY-LOSS")
            f.close()
        elif not self.is_spy() and spies_win:
            f = open("agent_results2.txt", "a")
            f.write(" RES-LOSS")
            f.close()
        elif not self.is_spy() and not spies_win:
            f = open("agent_results2.txt", "a")
            f.write(" RES-WIN")
            f.close()

            
        pass

    def critical_mission(self):
        '''
        Returns True if round can result in either a spy or resistance win False otherwise
        '''
        if self.rounds_complete == 4:
            return(True)
        elif self.missions_failed == 2:
            return(True)
        elif self.rounds_complete == 2 and self.missions_failed == 0:
            return(True)
        elif self.rounds_complete == 3 and self.missions_failed == 1:
            return(True)
        else:
            return(False)

