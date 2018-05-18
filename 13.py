with open('col1.txt') as f1, open('col2.txt') as f2:
  print([c1 + '\t' + c2 for c1, c2 in zip(f1, f2)])
