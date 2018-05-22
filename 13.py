with open('col1.txt') as f1, open('col2.txt') as f2:
  open('out.txt', 'w').writelines(''.join([c1.strip('\n') + '\t' + c2 for c1, c2 in zip(f1, f2)]))
