def ngram(s, n):
  l = []
  if isinstance(s, list):
    for i in s:
      l.extend(ngram(i, n))
  elif isinstance(s, str):
    if len(s) <= n:
      l.append(s)
    else:
      for i in range(len(s)):
        l.append(s[i:i+n])
  return l

s = 'I am an NLPer'

print(ngram(s, 2))
print(ngram(s.split(), 2))

print(ngram('paraparaparadise', 2))
print(ngram('paragraph', 2))
