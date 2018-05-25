import sys
argv = sys.argv
print(argv)
n = int(argv[1]) if len(argv) > 1 else -1
print (n)
with open('out.txt') as f:
    print(f.readlines()[:n])
