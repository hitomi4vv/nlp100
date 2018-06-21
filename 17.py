with open('hightemp.txt') as f:
    print('\n'.join(sorted(set([i[0] for i in [l.split() for l in f.read().splitlines()]]))))
