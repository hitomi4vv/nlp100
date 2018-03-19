def ngram(s, n):
  if isinstance(s, list):
    for i in s:
      ngram(i, n)
  elif isinstance(s, str):
    for i in range(len(s)):
      print(s[i:i+n])

s = 'I am an NLPer'
ngram(s, 2)
ngram(s.split(), 2)
