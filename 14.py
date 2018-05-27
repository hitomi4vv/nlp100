import sys
argv = sys.argv
print(argv)
with open('out.txt') as f:
    print(f.readlines()[:int(argv[1]) if len(argv) > 1 else -1])
