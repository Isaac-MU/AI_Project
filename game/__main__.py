from random_agent import RandomAgent
from AI2 import AI_Agent2
from AI import AI_Agent

from game import Game


f = open("agent_results.txt", "w")
f.write("")
f.close()

f = open("agent_results1.txt", "w")
f.write("")
f.close()


f = open("agent_results2.txt", "w")
f.write("")
f.close()

for k in range(1000):
        
        agents = [AI_Agent(name='AI1'), 
                AI_Agent2(name='AI2'),  
                AI_Agent(name='r3'),  
                AI_Agent(name='r4'),  
                AI_Agent2(name='r5'),  
                AI_Agent(name='r6')]

        game = Game(agents)
        game.play()

