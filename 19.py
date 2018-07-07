import collections
with open('hightemp.txt') as f:
    l = [i[0] for i in [l.split() for l in f.read().splitlines()]]
    print(collections.Counter(l))
    ll = collections.Counter(l).most_common()
    print('\n'.join('{0[1]} {0[0]}'.format(i) for i in ll))
