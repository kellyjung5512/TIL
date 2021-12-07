import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')

for tc in range(1, 11):
    T = int(input())
    find_txt = input()
    text = input()
    cnt = 0
    for i in range(len(text)-len(find_txt)+1):
        if text[i:len(find_txt)+i] == find_txt:
            cnt += 1
    print('#{} {}'.format(tc, cnt))