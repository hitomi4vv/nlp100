def ngram(s, n):
  if isinstance(s, list):
    for i in s:
      ngram(i, n)
  elif isinstance(s, str):
    print(s)

s = 'I am an NLPer'
ngram(s, 2)
ngram(s.split(), 2)
