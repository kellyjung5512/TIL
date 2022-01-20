import sys
sys.stdin = open('input.txt')

def dfs(arr):
    stack = [0]    # 출발점이 0부터라서 기본으로 넣어 줌

    while stack:
        temp = stack.pop()
        visited[temp] = 1

        if arr[temp]:
            for i in arr[temp]:
                stack.append(i)
    return visited[99]

for tc in range(1, 11):
    tc, road = map(int, input().split())
    num = list(map(int, input().split()))
    road_list = [[] for _ in range(100)]
    for i in range(road):
        road_list[num[i*2]].append(num[i*2+1])
    visited = [0] * 100
    print('#{} {}'.format(tc, dfs(road_list)))