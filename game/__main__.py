from random_agent import RandomAgent
from AI import AI_Agent
from game import Game


f = open("results.txt", "w")
f.write("")
f.close()

for k in range(1000):
        
        agents = [AI_Agent(name='AI'), 
                AI_Agent(name='r2'),  
                AI_Agent(name='r3'),  
                AI_Agent(name='r4'),  
                AI_Agent(name='r5'),  
                AI_Agent(name='r6'),  
                AI_Agent(name='r7')]

        game = Game(agents)
        game.play()
        print(game)