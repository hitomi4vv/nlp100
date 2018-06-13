import sys, itertools
with open('hightemp.txt') as f1:
  l = list(itertools.zip_longest(*[iter(f1.readlines())]*10))
  print(int(sys.argv[1]) if len(sys.argv) > 1 else 0)
  print(len(l))
  print('hightemp_{:02d}.txt'.format(4))
