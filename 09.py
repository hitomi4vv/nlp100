def typoglycemia(s):
  l= s.split()
  for c in l[1:len(l)-1]:
    if len(c) < 4:
      print(c)
  return l

print(typoglycemia("I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."))
