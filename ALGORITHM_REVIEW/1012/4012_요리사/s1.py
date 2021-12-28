import sys
sys.stdin = open('input.txt')

from itertools import combinations


def find_food(temp, count):
    if count == N//2:
        count_food()
        return

    for i in range(temp+1, N):
        if visited[i] == 0:
            visited.append(temp)
            find_food(i, count + 1)
            visited.pop()

def count_food():
    res = [0, 0]
    num_list = num_list - visited
    food_list = list(combinations(visited, 2))
    for i in range(len(food_list)):
        res[0] += foods[food_list[i][0]][food_list[i][1]]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    foods = [list(map(int, input().split())) for _ in range(N)]
    num_list = [i for i in range(N)]
    # a = list(permutations(num_list, N//2))
    # print(a)
    visited = []
    find_food(0, 1)
