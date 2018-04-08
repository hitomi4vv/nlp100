def cipher(s):
    ss = ''
    for c in s:
        ss += chr(219 - ord(c)) if c.islower() and c.isalpha() else c
    return ss

print(cipher('Hello world!'))
