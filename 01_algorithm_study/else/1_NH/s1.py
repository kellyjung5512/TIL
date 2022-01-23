import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    charList = list(map(str, input()))
    # 0 -> 48 1 -> 49, 9 -> 57
    # A -> 65 Z -> 90
    # a -> 97 z -> 122
    res = ''
    for char in charList:
        if ord(char) == 48:
            res += chr(48)
        elif 49 <= ord(char) <= 57:
             res += str(57 - ord(char) + 1)
        elif 65 <= ord(char) < 90:
            res += chr(ord(char) + 1)
        elif ord(char) == 90:
            res += 'A'
        elif 97 <= ord(char) <= 122:
            res += chr(122 - ord(char) + 97)
            # print('yes')
    print(res)