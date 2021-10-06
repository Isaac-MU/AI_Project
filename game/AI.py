from agent import Agent
import random

class AI_Agent(Agent):        
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
        self.suspicion = []    #array of size number_of_players to show the chances of them being spy from 0 to 1
        i = 0
        while i < number_of_players:
            if i != self.player_number:
                self.suspicion.append(len(self.spy_list)/(self.number_of_players - 1))
            else:
                self.suspicion.append(-1)
            i += 1
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
        if self.critical_mission():
            team.append(self.player_number)
        while len(team)<team_size:
            agent = random.randrange(team_size)
            if agent not in team:
                team.append(agent)
        return team        

    def vote(self, mission, proposer):
        '''
        mission is a list of agents to be sent on a mission. 
        The agents on the mission are distinct and indexed between 0 and number_of_players.
        proposer is an int between 0 and number_of_players and is the index of the player who proposed the mission.
        The function should return True if the vote is for the mission, and False if the vote is against the mission.
        '''
        vote = False
        if proposer == self.player_number:
            vote = True
        #If spy Only vote for critcal missions ie win or lose situation if spy is on
        elif self.is_spy() and self.critical_mission():
            for spy in self.spy_list:
                if spy in mission:
                    vote = True
        else:
            vote =  random.random()<0.5
        return(vote)

    def vote_outcome(self, mission, proposer, votes):
        '''
        mission is a list of agents to be sent on a mission. 
        The agents on the mission are distinct and indexed between 0 and number_of_players.
        proposer is an int between 0 and number_of_players and is the index of the player who proposed the mission.
        votes is a dictionary mapping player indexes to Booleans (True if they voted for the mission, False otherwise).
        No return value is required or expected.
        '''
        #nothing to do here
        pass

    def betray(self, mission, proposer):
        '''
        mission is a list of agents to be sent on a mission. 
        The agents on the mission are distinct and indexed between 0 and number_of_players, and include this agent.
        proposer is an int between 0 and number_of_players and is the index of the player who proposed the mission.
        The method should return True if this agent chooses to betray the mission, and False otherwise. 
        By default, spies will betray 30% of the time. 
        '''
        
        if self.is_spy() and self.critical_mission():
            return(True)
        else:
            return random.random()<0.3

    def mission_outcome(self, mission, proposer, betrayals, mission_success):
        '''
        mission is a list of agents to be sent on a mission. 
        The agents on the mission are distinct and indexed between 0 and number_of_players.
        proposer is an int between 0 and number_of_players and is the index of the player who proposed the mission.
        betrayals is the number of people on the mission who betrayed the mission, 
        and mission_success is True if there were not enough betrayals to cause the mission to fail, False otherwise.
        It iss not expected or required for this function to return anything.
        '''
        # For now only really works when not spy
        if not mission_success:
            agent = 0
            suspect_agents = [] #List of tuples containing suspect agent and current suspicion lvls
            non_suspect_agents = [] # Agents not on mission
            total_sus = 0 

            # if number of betrayals equals number of spies only agents that went on last mission can be spies
            if betrayals == self.number_of_spies:
                while agent < self.number_of_players:
                    if agent in mission and self.suspicion[agent] != -1:
                        suspect_agents.append((agent,self.suspicion[agent]))
                        total_sus += self.suspicion[agent]
                    else:
                        self.suspicion[agent] = -1 #Agent is not suspicious
                    agent += 1
                for suspect in suspect_agents:
                    self.suspicion[suspect[0]] = suspect[1]/total_sus

            else:
                betrayal_ratio = betrayals/ self.number_of_spies
                
                while agent < self.number_of_players:
                    if agent in mission and self.suspicion[agent] != -1:
                        suspect_agents.append((agent,self.suspicion[agent]))
                        total_sus += self.suspicion[agent]
                    elif self.suspicion[agent] != -1:
                        non_suspect_agents.append((agent,self.suspicion[agent]))
                    agent += 1

                # Will crash if total_sus = 0 (Prob due to agent being in mission with non suspicious agents and being a spy???)
                if total_sus == 0:
                    return(0)

                # total_sus == 1 also crashes I assume this means that the only suspicious agents went on the mission
                if total_sus == 1:
                    return(1)

                # Adjust the suspicion of agents on mission based on betrayels and amount on agents on mission
                suspicion_ratio = betrayal_ratio / total_sus
                total_non_sus = 1 - total_sus
                new_total_sus = 0

                for suspect in suspect_agents:
                    self.suspicion[suspect[0]] = suspect[1] * suspicion_ratio
                    new_total_sus += self.suspicion[suspect[0]]

                # Similarly adjust suspicion of agents not on mission
                new_total_non_sus = 1 - new_total_sus
                for non_suspect in non_suspect_agents:
                    non_sus_ratio = non_suspect[1] / total_non_sus
                    self.suspicion[non_suspect[0]] = non_sus_ratio * new_total_sus
        pass

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

