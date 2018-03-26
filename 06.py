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

x = set(ngram('paraparaparadise', 2))
y = set(ngram('paragraph', 2))
print(x)
print(y)
print(x.union(y))
