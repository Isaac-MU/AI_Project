from random_agent import RandomAgent
from AI import AI_Agent
from dylan_ai import AI_Agent2

from game import Game



f = open("agent_results2.txt", "w")
f.write("")
f.close()
        
agents = [AI_Agent(name='AI'), 
        AI_Agent2(name='r2'),  
        RandomAgent(name='r3'),  
        RandomAgent(name='r4'),  
        RandomAgent(name='r5'),  
        RandomAgent(name='r6'),  
        RandomAgent(name='r7')]

game = Game(agents)
game.play()
print(game)


