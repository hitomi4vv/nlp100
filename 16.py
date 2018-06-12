import itertools
with open('hightemp.txt') as f:
  print(list(itertools.zip_longest(*[iter(f.readlines())]*10)))
