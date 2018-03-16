def ngram(s, n):
  print(s)
  print(len(s))
  print(type(s))
  print(isinstance(s, str))
  print(isinstance(s, list))

s = 'I am an NLPer'
ngram(s, 2)
ngram(s.split(), 2)
