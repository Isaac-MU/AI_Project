
from AI import AI_Agent
from baye import bayes_rule

from game import Game


f = open("results.txt", "w")
f.write("")
f.close()

num = int(input("Game Size?:"))
c = input("Should AI be spies or resistance S/R?:")
if c != 'R' and c != 'r' and  c != 's' and  c != 'S':
        exit()
if num == 5:

        for k in range(1000):
        
                agents = [bayes_rule(name='AI'), 
                bayes_rule(name='AI'),   
                AI_Agent(name='R'),
                AI_Agent(name='R')]
                if c == 'r' or c == 'R':
                        agents.append(bayes_rule(name='AI'))
                else:
                        agents.append(AI_Agent(name='R'))


                game = Game(agents,c)
                game.play()
                print(game)

if num == 6:

        for k in range(1000):
        
                agents = [AI_Agent(name='AI'), 
                AI_Agent(name='AI'),  
                bayes_rule(name='R'),
                bayes_rule(name='R')]
                if c == 'r' or c == 'R':
                        agents.append(AI_Agent(name='AI'))
                        agents.append(AI_Agent(name='AI'))
                else:
                        agents.append(bayes_rule(name='R'))
                        agents.append(bayes_rule(name='R'))

                game = Game(agents,c)
                game.play()
                print(game)

if num == 7:

        for k in range(1000):
        
                agents = [AI_Agent(name='AI'), 
                AI_Agent(name='AI'),  
                AI_Agent(name='AI'),  
                bayes_rule(name='R'),
                bayes_rule(name='R'),
                bayes_rule(name='R')]
                if c == 'r' or c == 'R':
                        agents.append(AI_Agent(name='AI'))
                else:
                        agents.append(bayes_rule(name='R'))

                game = Game(agents,c)
                game.play()
                print(game)

if num == 8:

        for k in range(1000):
        
                agents = [AI_Agent(name='AI'), 
                AI_Agent(name='AI'),  
                AI_Agent(name='AI'),  
                bayes_rule(name='R'),
                bayes_rule(name='R'),
                bayes_rule(name='R')]
                if c == 'r' or c == 'R':
                        agents.append(AI_Agent(name='AI'))
                        agents.append(AI_Agent(name='AI'))
                else:
                        agents.append(bayes_rule(name='R'))
                        agents.append(bayes_rule(name='R'))

                game = Game(agents,c)
                game.play()
                print(game)

if num == 9:

        for k in range(1000):
        
                agents = [AI_Agent(name='AI'), 
                AI_Agent(name='AI'),  
                AI_Agent(name='AI'),  
                bayes_rule(name='R'),
                bayes_rule(name='R'),
                bayes_rule(name='R')]
                if c == 'r' or c == 'R':
                        agents.append(AI_Agent(name='AI'))
                        agents.append(AI_Agent(name='AI'))
                        agents.append(AI_Agent(name='AI'))
                else:
                        agents.append(bayes_rule(name='R'))
                        agents.append(bayes_rule(name='R'))
                        agents.append(bayes_rule(name='R'))

                game = Game(agents,c)
                game.play()
                print(game)

if num == 10:

        for k in range(1000):
        
                agents = [AI_Agent(name='AI'), 
                AI_Agent(name='AI'),  
                AI_Agent(name='AI'),
                AI_Agent(name='AI'),  
                bayes_rule(name='R'),
                bayes_rule(name='R'),
                bayes_rule(name='R'),
                bayes_rule(name='R')]
                if c == 'r' or c == 'R':
                        agents.append(AI_Agent(name='AI'))
                        agents.append(AI_Agent(name='AI'))
                else:
                        agents.append(bayes_rule(name='R'))
                        agents.append(bayes_rule(name='R'))


                game = Game(agents,c)
                game.play()
                print(game)
else:
        exit()
