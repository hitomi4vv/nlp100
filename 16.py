import sys, itertools
with open('hightemp.txt') as f:
  for i, j in enumerate(itertools.zip_longest(*[iter(f.readlines())] * (int(sys.argv[1]) if len(sys.argv) > 1 else 1))):
    open('hightemp_{:02d}.txt'.format(i), 'w').writelines(''.join(filter(None, j)))
