import sys
sys.stdin = open('input.txt')


def find_max(arr):
    ans = 1
    for a in range(len(arr)):
        cnt = 1
        for b in range(1, len(arr)):
            if arr[a][b] == arr[a][b-1]:
                cnt += 1
            else:
                cnt = 1

            if cnt > ans:
                ans = cnt

        if ans == len(arr):
            return ans

        cnt = 1
        for b in range(1, len(arr)):
            if arr[b][a] == arr[b-1][a]:
                cnt += 1
            else:
                cnt = 1

            if cnt > ans:
                ans = cnt

        if ans == len(arr):
            return ans

    return ans

num = int(input())
candy_list = [list(map(str, input())) for _ in range(num)]
result = 0

for i in range(num):
    for j in range(num):
        # 오른쪽으로 갈 때
        # '범위를 넘지 않으면'이라는 조건이 있을 때
        if j+1 < num:
            if candy_list[i][j] != candy_list[i][j+1]:
                candy_list[i][j], candy_list[i][j+1] = candy_list[i][j+1], candy_list[i][j]

                temp = find_max(candy_list)

                if temp > result:
                    result = temp

                # 돌려놓기
                candy_list[i][j], candy_list[i][j+1] = candy_list[i][j+1], candy_list[i][j]


        # 아래쪽으로 갈 때
        if i+1 < num:
            if candy_list[i][j] != candy_list[i+1][j]:
                candy_list[i][j], candy_list[i+1][j] = candy_list[i+1][j], candy_list[i][j]

                temp = find_max(candy_list)

                if temp > result:
                    result = temp

                # 돌려놓기
                candy_list[i][j], candy_list[i + 1][j] = candy_list[i + 1][j], candy_list[i][j]


print(result)