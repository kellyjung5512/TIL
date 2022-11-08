import sys
sys.stdin = open("input.txt")

book_index = list(map(str, input().split(", ")))
# book_index.sort()
# print(book_index)
version = []
for index in book_index:
    x, y, z = map(int, index.split("."))
    version.append([x, y, z])
version.sort(key=lambda x: (x[0], x[1], x[2]))
print(version)

# [[1,2],[2,3]]
# version.sort(key=lambda x: x[1])

help(sort())