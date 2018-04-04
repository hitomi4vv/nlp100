def cipher(s):
  for c in s:
    print(c.islower())
  return s

def decipher(s):
  for c in s:
    print(c)
  return s

print(cipher('Hello world!'))
print(decipher('Hello world!'))
