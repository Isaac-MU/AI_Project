from random_agent import RandomAgent
from AI2 import AI_Agent
from game import Game

f = open("agent_results.txt", "w")
f.write("")
f.close()

for k in range(10000):
        
        agents = [AI_Agent(name='AI'), 
                RandomAgent(name='r2'),  
                RandomAgent(name='r3'),  
                RandomAgent(name='r4'),  
                RandomAgent(name='r5'),  
                RandomAgent(name='r6'),  
                RandomAgent(name='r7')]

        game = Game(agents)
        game.play()

