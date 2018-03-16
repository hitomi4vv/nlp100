def ngram(s, n):
  if isinstance(s, str):
    for char in s:
      print(char)
  elif isinstance(s, list):
    for i in s:
      ngram(i, n)

s = 'I am an NLPer'
ngram(s, 2)
ngram(s.split(), 2)
