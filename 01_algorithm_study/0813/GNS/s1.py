import sys
sys.stdin = open('input.txt')

# numbers = {'ZRO' : 0,
#            'ONE' : 1,
#            'TWO' : 2,
#            'THR' : 3,
#            'FOR' : 4,
#            'FIV' : 5,
#            'SIX' : 6,
#            'SVN' : 7,
#            'EGT' : 8,
#            'NIN' : 9}
numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

T = int(input())
for tc in range(1, T+1):
    num, tclen = map(str, input().split())
    temp = list(map(str, input().split()))
    check = [0] * 10
    ans = []
    for i in range(int(tclen)):
        if temp[i] in numbers:
            check[numbers.index(temp[i])] += 1
    # print(check)
    for j in range(10):
        for k in range(check[j]):
            ans.append(numbers[j])
    print(num)
    print(*ans)
