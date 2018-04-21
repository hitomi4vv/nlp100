import random

def shuffle(s):
    l = list(s)
    random.shuffle(l)
    return ''.join(l)

def typoglycemia(s):
  l = s.split()
  return ' '.join([c[0] + shuffle(list(c)[1:len(c)-1]) + c[len(c)-1] if len(c) > 4 else c for c in l])

s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(typoglycemia(s))
