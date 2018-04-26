f = open('hightemp.txt')
s = [l.split() for l in f.read().splitlines()]
f.close()
with open('col1.txt', 'w') as f:
    f.write('\n'.join([i[0] for i in s]))
f.close()
with open('col2.txt', 'w') as f:
    f.write('\n'.join([i[1] for i in s]))
f.close()
