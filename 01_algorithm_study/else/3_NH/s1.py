import sys
sys.stdin = open('input.txt')

from itertools import permutations

def Mydivision(num):
    for i in range(2, int(num**(1/2))+1):
        if n % i == 0:
            divisionList.append(i)
            if i**2 != num:
                divisionList.append(n//i)
    divisionList.sort(reverse=True)

def find_maxi():
    global result
    for step in divisionList:
        pointList = []
        for i in range(0, n, step):
            pointList.append(i)
        pointList = pointList * 2
        startPointList = set(list(permutations(pointList, 2)))
        # print(startPointList)
        ans = 0
        for x, y in startPointList:
            check_dict = {}
            for j in range(x, x + step):
                for k in range(y, y + step):
                    temp = arr[j][k]
                    if temp in check_dict:
                        check_dict[temp] += 1
                    else:
                        check_dict[temp] = 1
            if len(check_dict) <= t:
                ans += 1
            else:
                break
        if ans == len(startPointList):
            result = step
            break

T = int(input())
for tc in range(1, T+1):
    result = 0
    n = int(input())
    t = int(input())
    divisionList = []
    arr = [list(map(str, input())) for _ in range(n)]
    Mydivision(n)
    if len(divisionList) == 0:
        print('#{} {}'.format(tc, result))
        break
    else:
        find_maxi()
        print('#{} {}'.format(tc, result))


# scores = {"철수": 90, "민수": 85, "영희": 80}
# print(scores["철수"])