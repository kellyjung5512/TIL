cnt = int(input())
number_list = []
for i in range(cnt) :
    [x, y] = map(int, input().split())
    number_list.append([x, y])

number_list.sort()

for j in number_list :
    print(j[0], j[1])