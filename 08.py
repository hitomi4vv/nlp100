def cipher(s):
  for c in s:
    if c.islower() and c.isalpha():
        print(219 - ord(c))
  return s

def decipher(s):
  for c in s:
    print(c)
  return s

print(cipher('Hello world!'))
print(decipher('Hello world!'))
