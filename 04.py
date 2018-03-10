s = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
n = [1, 5, 6, 7, 8, 9, 15, 16, 19]
l = s.split()
print([(v[:1], i) if i in n else (v[:2], i) for i, v in enumerate(l, 1)])
