import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
res = 0
have_word = [97, 110, 116, 105, 99]
for tc in range(N):
    find_word = input()
    if len(find_word) > 0:
        word = list(find_word)[4:-4]
    else:
        continue
    # print(word)
    # print(ord('c'))
    # a = 97, n = 110, t = 116, i = 105, c = 99


    cnt = len(have_word)
    for i in range(len(word)):
        ord_word = ord(word[i])
        if ord_word in have_word:
            continue
        else:
            if cnt < K:
                cnt += 1
                have_word.append(ord_word)
            else:
                cnt = 0
                break

    if cnt > 0:
        res += 1
    else:
        pass

print(res)