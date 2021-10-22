from agent import Agent
import random

class bayes_rule(Agent):        
    '''A sample implementation of a decision tree agent in the game The Resistance'''

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

        #getting the number of spies
        if number_of_players == 5 or number_of_players == 6:
            self.number_of_spies = 2
        elif number_of_players == 7 or  number_of_players == 8 or number_of_players == 9:
            self.number_of_spies = 3
        elif number_of_players == 10:
            self.number_of_spies = 4
        
        self.initialised = False
        self.teams_with_me = []
        self.possible_teams = []


        #generates all possible spy teams to later keep tabs on
        possible_spy_teams = []

        if self.number_of_spies == 2:
            for i in number_of_players:
                for k in number_of_players:

                    if i != k:
                        possible_team = [i,k]
                        possible_team.sort()
                        if possible_team not in possible_spy_teams:
                            possible_spy_teams.append(possible_team)


        if self.number_of_spies == 3:
            for i in number_of_players:
                for k in number_of_players:
                    for n in number_of_players:

                        if i != k and i != n and k != n:
                            possible_team = [i,k,n]
                            possible_team.sort()
                            if possible_team not in possible_spy_teams:
                                possible_spy_teams.append(possible_team)


        if self.number_of_spies == 4:
            for i in number_of_players:
                for k in number_of_players:
                    for n in number_of_players:
                        for x in number_of_players:

                            if i != k and i != n and i != x and k != n and k != x and n != x:
                                possible_team = [i,k,n,x]
                                possible_team.sort()
                                if possible_team not in possible_spy_teams:
                                    possible_spy_teams.append(possible_team)


        #A dictionary containing the probability of each spy team existing
        #Initially all probabilities are equal (1/number of possbile teams)
        self.spy_team_probability = {}
        for i in range(len(possible_spy_teams)):
            self.spy_team_probability[possible_spy_teams[i]] = 1/len(possible_spy_teams)

        #A dictionary containing the probability of each player being a spy
        #Initially all probabilities are equal (1/number of possbile teams)
        self.spy_probability = {}
        for i in range(number_of_players):
            self.spy_probability[i] = 1/len(number_of_players)



    def is_spy(self):
        '''
        returns True iff the agent is a spy
        '''
        pass

    def propose_mission(self, team_size, betrayals_required = 1):
        '''
        expects a team_size list of distinct agents with id between 0 (inclusive) and number_of_players (exclusive)
        to be returned. 
        betrayals_required are the number of betrayals required for the mission to fail.
        '''


        if not self.initialised:
            #generates all possible teams

            if team_size == 2:
                for i in self.number_of_players:
                    for k in self.number_of_players:

                        if i != k:
                            possible_team = [i,k]
                            possible_team.sort()
                            if possible_team not in self.possible_teams:
                                self.possible_teams.append(possible_team)


            if self.number_of_spies == 3:
                for i in self.number_of_players:
                    for k in self.number_of_players:
                        for n in self.number_of_players:

                            if i != k and i != n and k != n:
                                possible_team = [i,k,n]
                                possible_team.sort()
                                if possible_team not in self.possible_teams:
                                    self.possible_teams.append(possible_team)


            if self.number_of_spies == 4:
                for i in self.number_of_players:
                    for k in self.number_of_players:
                        for n in self.number_of_players:
                            for x in self.number_of_players:

                                if i != k and i != n and i != x and k != n and k != x and n != x:
                                    possible_team = [i,k,n,x]
                                    possible_team.sort()
                                    if possible_team not in self.possible_teams:
                                        self.possible_teams.append(possible_team)


            #A dictionary containing the probability of each team betraying
            #Initially all probabilities are equal (1/number of possbile teams)
            self.team_probability = {}
            for i in range(len(self.possible_teams)):
                self.team_probability[self.possible_teams[i]] = 1/len(self.possible_teams)

            #Finds all the teams that i am on
            for i in self.possible_teams:
                if self.player_number in i:
                    self.teams_with_me.append(i)

            self.initialised = True

            #since we dont have any info on which team could be dangerous, just choose a random one with me on it
            return random.choice(self.teams_with_me)


        #Gets what i think the spy team is
        key_list = list(self.spy_team_probability.keys())
        val_list = list(self.spy_team_probability.values())
        position = val_list.index(max(val_list))
        most_dangerous_team = key_list[position]


        #Will chose a team i am on, and the suspected spies are not on
        team_clean = True
        for team in self.teams_with_me:
            for team_member in team:
                if team_member in most_dangerous_team:
                    team_clean = False
            if team_clean:
                return team

        #If i cant find a team where the suspects aren't on, ill just chose a random team.
        return random.choice(self.teams_with_me)

            
    def vote(self, mission, proposer):
        '''
        mission is a list of agents to be sent on a mission. 
        The agents on the mission are distinct and indexed between 0 and number_of_players.
        proposer is an int between 0 and number_of_players and is the index of the player who proposed the mission.
        The function should return True if the vote is for the mission, and False if the vote is against the mission.
        '''
        
        
        #Vote for my own missions
        if proposer == self.player_number:
            return True

        #If there is more people on mission than possible spies, and im not on the mission
        #Then there has to be a spy on the mission, so we vote no
        if (len(mission) >= self.number_of_players - self.number_of_spies) and (self.player_number not in mission):
            return False
            
        #Gets what i think the spy team is
        key_list = list(self.spy_team_probability.keys())
        val_list = list(self.spy_team_probability.values())
        position = val_list.index(max(val_list))
        most_dangerous_team = key_list[position]

        #If a suspected spy is on the team, vote no
        for player in most_dangerous_team:
            if player in mission:
                return False

        #If the proposer is suspected to be a spy, dont trust their vote
        if proposer in most_dangerous_team:
            return False
        
        #All saftey checks passed, vote yes
        return True


    def vote_outcome(self, mission, proposer, votes):
        '''
        mission is a list of agents to be sent on a mission. 
        The agents on the mission are distinct and indexed between 0 and number_of_players.
        proposer is an int between 0 and number_of_players and is the index of the player who proposed the mission.
        votes is a dictionary mapping player indexes to Booleans (True if they voted for the mission, False otherwise).
        No return value is required or expected.
        '''
        pass

    def betray(self, mission, proposer):
        '''
        mission is a list of agents to be sent on a mission. 
        The agents on the mission are distinct and indexed between 0 and number_of_players, and include this agent.
        proposer is an int between 0 and number_of_players and is the index of the player who proposed the mission.
        The method should return True if this agent chooses to betray the mission, and False otherwise. 
        By default, spies will betray 30% of the time. 
        '''
        return self.is_spy()

    def mission_outcome(self, mission, proposer, betrayals, mission_success):
        '''
        mission is a list of agents to be sent on a mission. 
        The agents on the mission are distinct and indexed between 0 and number_of_players.
        proposer is an int between 0 and number_of_players and is the index of the player who proposed the mission.
        betrayals is the number of people on the mission who betrayed the mission, 
        and mission_success is True if there were not enough betrayals to cause the mission to fail, False otherwise.
        It iss not expected or required for this function to return anything.
        '''
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

