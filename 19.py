import collections
with open('hightemp.txt') as f:
    print('\n'.join('{0[1]} {0[0]}'.format(i) for i in collections.Counter([i[0] for i in [l.split() for l in f.read().splitlines()]]).most_common()))
