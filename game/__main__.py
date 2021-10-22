from random_agent import RandomAgent
from AI import AI_Agent
from dylan_ai import AI_Agent2
from bayes_rule import bayes_rule
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

for i in range(1000):
        agents = [AI_Agent(name='AI'), 
                AI_Agent(name='r2'),  
                AI_Agent(name='r3'),  
                bayes_rule(name='r4'),  
                AI_Agent(name='r5'),  
                bayes_rule(name='r7')]

        game = Game(agents)
        game.play()


