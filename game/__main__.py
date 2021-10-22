from random_agent import RandomAgent
from AI import AI_Agent
from dylan_ai import AI_Agent2

from game import Game


f = open("results.txt", "w")
f.write("")
f.close()

num = int(input("Game Size?:"))
c = input("Should AI be spies or resistance S/R?:")
if c != 'R' and c != 'r' and  c != 's' and  c != 'S':
        exit()
if num == 5:

        for k in range(3000):
        
                agents = [AI_Agent(name='AI'), 
                AI_Agent(name='AI'),   
                RandomAgent(name='R'),
                RandomAgent(name='R')]
                if c == 'r' or c == 'R':
                        agents.append(AI_Agent(name='AI'))
                else:
                        agents.append(RandomAgent(name='R'))


                game = Game(agents,c)
                game.play()
                print(game)

if num == 6:

        for k in range(3000):
        
                agents = [AI_Agent(name='AI'), 
                AI_Agent(name='AI'),  
                RandomAgent(name='R'),
                RandomAgent(name='R')]
                if c == 'r' or c == 'R':
                        agents.append(AI_Agent(name='AI'))
                        agents.append(AI_Agent(name='AI'))
                else:
                        agents.append(RandomAgent(name='R'))
                        agents.append(RandomAgent(name='R'))

                game = Game(agents,c)
                game.play()
                print(game)

if num == 7:

        for k in range(3000):
        
                agents = [AI_Agent(name='AI'), 
                AI_Agent(name='AI'),  
                AI_Agent(name='AI'),  
                RandomAgent(name='R'),
                RandomAgent(name='R'),
                RandomAgent(name='R')]
                if c == 'r' or c == 'R':
                        agents.append(AI_Agent(name='AI'))
                else:
                        agents.append(RandomAgent(name='R'))

                game = Game(agents,c)
                game.play()
                print(game)

if num == 8:

        for k in range(3000):
        
                agents = [AI_Agent(name='AI'), 
                AI_Agent(name='AI'),  
                AI_Agent(name='AI'),  
                RandomAgent(name='R'),
                RandomAgent(name='R'),
                RandomAgent(name='R')]
                if c == 'r' or c == 'R':
                        agents.append(AI_Agent(name='AI'))
                        agents.append(AI_Agent(name='AI'))
                else:
                        agents.append(RandomAgent(name='R'))
                        agents.append(RandomAgent(name='R'))

                game = Game(agents,c)
                game.play()
                print(game)

if num == 9:

        for k in range(3000):
        
                agents = [AI_Agent(name='AI'), 
                AI_Agent(name='AI'),  
                AI_Agent(name='AI'),  
                RandomAgent(name='R'),
                RandomAgent(name='R'),
                RandomAgent(name='R')]
                if c == 'r' or c == 'R':
                        agents.append(AI_Agent(name='AI'))
                        agents.append(AI_Agent(name='AI'))
                        agents.append(AI_Agent(name='AI'))
                else:
                        agents.append(RandomAgent(name='R'))
                        agents.append(RandomAgent(name='R'))
                        agents.append(RandomAgent(name='R'))

<<<<<<< Updated upstream
                game = Game(agents,c)
                game.play()
                print(game)
=======
for i in range(10):
        agents = [AI_Agent2(name='AI'), 
                AI_Agent2(name='r2'),  
                AI_Agent2(name='r3'),  
                bayes_rule(name='r4'),  
                AI_Agent2(name='r5'),  
                bayes_rule(name='r7')]
>>>>>>> Stashed changes

if num == 10:

        for k in range(3000):
        
                agents = [AI_Agent(name='AI'), 
                AI_Agent(name='AI'),  
                AI_Agent(name='AI'),
                AI_Agent(name='AI'),  
                RandomAgent(name='R'),
                RandomAgent(name='R'),
                RandomAgent(name='R'),
                RandomAgent(name='R')]
                if c == 'r' or c == 'R':
                        agents.append(AI_Agent(name='AI'))
                        agents.append(AI_Agent(name='AI'))
                else:
                        agents.append(RandomAgent(name='R'))
                        agents.append(RandomAgent(name='R'))


                game = Game(agents,c)
                game.play()
                print(game)
else:
        exit()
