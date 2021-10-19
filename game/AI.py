from agent import Agent
import random

class AI_Agent(Agent):        
    '''A sample implementation of a random agent in the game The Resistance'''

    def __init__(self, name='AI_agent'):
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
        #If not spy no need to track suspcion of AI agent
        if not self.is_spy():

            while i < number_of_players:
                if i != self.player_number:
                    self.suspicion.append(len(self.spy_list)/(self.number_of_players - 1))
                else:
                    self.suspicion.append(-1)
                i += 1
        else:
            while i < number_of_players:
                    self.suspicion.append(len(self.spy_list)/(self.number_of_players))
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
        suspectIndex = [] #List of tuples containng index of agent and suspect lvl
        index = 0
        for agent in self.suspicion:
            suspectIndex.append((agent,index))
            index += 1

        suspectIndex.sort() # Sort by suspicion in acending order

        # If not spy always put least suspicious agents on mission
        if not self.is_spy():
            i = 0
            while len(team)<team_size:
                team.append(suspectIndex[i][1])
                i += 1
        # If spy put the least suspcious spy on mission 
        # And most suspicous agents
        else:

            for a in suspectIndex:
                #First spy is least suspicous
                if a[1] in self.spy_list:
                    team.append(a[1])

                    if self.number_of_players <= 6 or self.rounds_complete != 3: #Two may be spies required
                        break
                    elif len(team) == 2:
                        break

            suspectIndex.sort(reverse=True) # Sort by suspicion in decending order
            
            for a in suspectIndex:
                if a[1] not in self.spy_list:
                    team.append(a[1])
                    if team == team_size:
                        break
        return team        

    def vote(self, mission, proposer):
        '''
        mission is a list of agents to be sent on a mission. 
        The agents on the mission are distinct and indexed between 0 and number_of_players.
        proposer is an int between 0 and number_of_players and is the index of the player who proposed the mission.
        The function should return True if the vote is for the mission, and False if the vote is against the mission.
        '''
        vote = False
        suspectIndex = [] #List of tuples containng index of agent and suspect lvl
        index = 0
        for agent in self.suspicion:
            suspectIndex.append((agent,index))
            index += 1

        suspectIndex.sort(reverse=True) # Sort by suspicion in decending order

        #Obviously vote for missions agent proposed
        if proposer == self.player_number:
            vote = True
        #If spy Only vote for critcal missions ie win or lose situation if spy is on
        elif self.is_spy() and self.critical_mission():
            for spy in self.spy_list:
                if spy in mission:
                    vote = True
        #If not spy vote for missions if most suspcious agents aren't on
        elif not self.is_spy():
            vote = True
            suspects = [] # list of most suspcious agents length of number of spies
            i = 0

            while len(suspects) != self.number_of_spies:
                suspects.append(suspectIndex[i][1])

            for a in mission:
                 if a in suspects:
                    vote = False
            
        #If spy only vote for missions with minimum number of spies needed to fail mission
        # and not most suspect spy
        else:
            suspectIndex.sort()# Sort in acedning order
            vote = True
            susSpy = -1 #Most suspcious spy
            spyCount = 0
            for suspect in suspectIndex:
                if suspect[1] in self.spy_list:
                    susSpy = suspect
            for a in mission:
                if a == susSpy:
                    vote = False
                    break
                if a in self.spy_list:
                    spyCount += 1
            if self.number_of_players > 6 or self.rounds_complete == 3 and spyCount != 2:
                vote = False
            elif spyCount != 1:
                vote = False

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
        averageSuspicion = 1 / self.number_of_players
        suspectIndex = [] #List of tuples containng index of agent in mission and suspect lvl
        index = 0
        for a in self.suspicion:
            if index in mission:
                suspectIndex.append((a,index))
            index += 1
        suspectIndex.sort(reverse=True) # Sort by suspicion in decending order

        spies = []#Spies in mission 
        for agent in mission:
                if agent in self.spy_list:
                    spies.append(agent)

        if self.critical_mission():
            return(True)

        #Dont betray if only spy on mission where 2 betrayals needed
        elif self.number_of_players > 6 or self.rounds_complete == 3:
            if len(spies) == 1:
                return(False)

        #Dont betray if all spies are on mission
        elif len(spies) == self.number_of_spies:
            return(False)

        #Only betray if suspicion of all spies on mission is less than average or 
        #There is a more suspicious non spy
        else:
            for ag in suspectIndex:
                if ag[1] in mission and ag[1] in spies:
                    break
                elif ag[1] in mission:
                    return(True)
            betray = True
            for ag in suspectIndex:
                if ag[1] in spies and ag[0] > averageSuspicion:
                    betray = False
            return(betray)

    def mission_outcome(self, mission, proposer, betrayals, mission_success):
        '''
        mission is a list of agents to be sent on a mission. 
        The agents on the mission are distinct and indexed between 0 and number_of_players.
        proposer is an int between 0 and number_of_players and is the index of the player who proposed the mission.
        betrayals is the number of people on the mission who betrayed the mission, 
        and mission_success is True if there were not enough betrayals to cause the mission to fail, False otherwise.
        It iss not expected or required for this function to return anything.
        '''

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
                    if total_sus == 0:
                        self.suspicion[suspect[0]] = 1
                    else:
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
        
        if self.is_spy() and spies_win:
            f = open("agent_results.txt", "a")
            f.write(" WIN")
            f.close()
        elif self.is_spy() and not spies_win:
            f = open("agent_results.txt", "a")
            f.write(" LOSS")
            f.close()
        elif not self.is_spy() and spies_win:
            f = open("agent_results.txt", "a")
            f.write(" LOSS")
            f.close()
        elif not self.is_spy() and not spies_win:
            f = open("agent_results.txt", "a")
            f.write(" WIN")
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

