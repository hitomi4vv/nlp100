with open('hightemp.txt') as f:
    print(''.join(sorted(f.readlines(), key = lambda x: x.split()[2], reverse = True)), end = '')
