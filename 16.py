import sys, itertools
with open('hightemp.txt') as f1:
  for i, j in enumerate(itertools.zip_longest(*[iter(f1.readlines())] * int(sys.argv[1]) if len(sys.argv) > 1 else len(f1.readlines()))):
    open('hightemp_{:02d}.txt'.format(i), 'w').writelines(''.join(filter(None, j)))
