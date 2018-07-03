import collections
with open('hightemp.txt') as f:
    print(collections.Counter([i[0] for i in [l.split() for l in f.read().splitlines()]]).most_common())
