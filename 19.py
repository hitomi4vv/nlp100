import collections
with open('hightemp.txt') as f:
    l = [i[0] for i in [l.split() for l in f.read().splitlines()]]
    print(collections.Counter(l))
    print(collections.Counter(l).most_common())
