with open('hightemp.txt') as f:
    s = [l.split() for l in f.read().splitlines()]
with open('col1.txt', 'w') as f:
    f.write('\n'.join([i[0] for i in s]))
with open('col2.txt', 'w') as f:
    f.write('\n'.join([i[1] for i in s]))
