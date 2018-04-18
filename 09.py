import random

def typoglycemia(s):
  l = s.split()
  return ' '.join(['hoge' if len(c) > 4 else c for c in l])

s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(typoglycemia(s))
