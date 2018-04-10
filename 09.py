def typoglycemia(s):
  l = [len(c) for c in s.split()]
  print(l)
  return s.split()

print(typoglycemia("I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."))
