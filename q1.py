import sys

a = input()

for line in sys.stdin:
    line = line.strip()
    print(len(line)+1)
