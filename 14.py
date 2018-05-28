import sys
argv = sys.argv
with open('out.txt') as f:
    print(''.join(f.readlines()[:int(argv[1]) if len(argv) > 1 else -1]), end = '')
