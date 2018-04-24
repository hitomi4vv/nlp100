f = open('hightemp.txt')
s = [l.split() for l in f.read().splitlines()]
f.close()
print([i[0] for i in s])
print([i[1] for i in s])
