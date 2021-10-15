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

