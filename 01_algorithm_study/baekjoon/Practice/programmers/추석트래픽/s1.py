import sys
sys.stdin = open("input.txt")

versions = list(map(str, input().split(", ")))
version_index = []
for version in versions:
    x, y, z = map(int, version.split("."))
    version_index.append([x, y, z])
version_index.sort(key=lambda x: (x[0], x[1], x[2]))
print(version_index)