import collections
with open('hightemp.txt') as f:
    print('\n'.join(collections.Counter(sorted([i[0] for i in [l.split() for l in f.read().splitlines()]])).most_common()))
