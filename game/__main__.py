from random_agent import RandomAgent
from AI2 import AI_Agent2
from AI import AI_Agent1

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

for k in range(10000):
        
        agents = [AI_Agent1(name='AI1'), 
                AI_Agent2(name='AI2'),  
                AI_Agent1(name='r3'),  
                AI_Agent2(name='r4'),  
                AI_Agent1(name='r5'),  
                AI_Agent2(name='r6'),  
                RandomAgent(name='r7')]

        game = Game(agents)
        game.play()

