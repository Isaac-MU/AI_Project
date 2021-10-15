from random_agent import RandomAgent
from AI import AI_Agent
from game import Game


f = open("results.txt", "w")
f.write("")
f.close()

def test_1():   
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

        f = open("results.txt", "r")
        data = f.read()
        words = data.split()
        print(len(words)) 
        spy_count = 0
        res_count = 0
        for k in words:
                if k == 'SPY':
                        spy_count += 1
                if k == 'RES':
                        res_count += 1
        print('SPY: ', spy_count)
        print('RES: ', res_count)
        return(spy_count, res_count)
#test_1()

agents = [AI_Agent(name='AI1'), 
         RandomAgent(name='r2'),  
        RandomAgent(name='r3'),  
        RandomAgent(name='r4'),
        RandomAgent(name='r5'),
        ]
game = Game(agents)
game.play()
print(game)