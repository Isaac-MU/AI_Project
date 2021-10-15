from random_agent import RandomAgent
from AI import AI_Agent
from game import Game


f = open("results.txt", "w")
f.write("")
f.close()

for k in range(1000):
        
        agents = [AI_Agent(name='AI1'), 
                AI_Agent(name='AI2'),  
                AI_Agent(name='r3'),  
                RandomAgent(name='r4'),
                RandomAgent(name='r5'),
                 ]

        game = Game(agents)
        game.play()
        print(game)