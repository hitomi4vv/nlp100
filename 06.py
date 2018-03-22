def ngram(s, n):
  if isinstance(s, list):
    for i in s:
      ngram(i, n)
  elif isinstance(s, str):
    if len(s) <= n:
      print(s)
    else:
      for i in range(len(s)):
        print(s[i:i+n])

ngram('paraparaparadise', 2)
ngram('paragraph', 2)
