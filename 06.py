def ngram(s, n):
  l = []
  if isinstance(s, list):
    for i in s:
      ngram(i, n)
  elif isinstance(s, str):
    if len(s) <= n:
      l.append(s)
    else:
      for i in range(len(s)):
        l.append(s[i:i+n])
  return l

print(ngram('paraparaparadise', 2))
print(ngram('paragraph', 2))
