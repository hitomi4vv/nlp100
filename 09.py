import random
def typoglycemia(s):
  l = s.split()
  l = [random.shuffle(c.split()) if len(c) > 4 else c for c in l]
  print(l)
  return l

s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
typoglycemia(s)
# print(s)
