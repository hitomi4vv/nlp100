import sys
with open('hightemp.txt') as f:
    print(''.join(f.readlines()[:int(sys.argv[1]) if len(sys.argv) > 1 else -1]), end = '')
