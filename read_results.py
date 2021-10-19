
def overall_results():
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


def AI_results():
    f = open("agent_results.txt", "r")
    data = f.read()
    words = data.split()
    print(len(words)) 
    win_count = 0
    loss_count = 0
    for k in words:
        if k == 'WIN':
            win_count += 1
        if k == 'LOSS':
            loss_count += 1
    print('WINS: ', win_count)
    print('LOSSES: ', loss_count)

AI_results()
overall_results()