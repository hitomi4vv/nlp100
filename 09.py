def typoglycemia(s):
  l = s.split()
  print([c for c in l if len(c) > 4])
  return l

s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
typoglycemia(s)
print(s)
