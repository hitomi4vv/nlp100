with open('hightemp.txt') as f:
  print(list(zip(*[iter(f.readlines())]*10)))
