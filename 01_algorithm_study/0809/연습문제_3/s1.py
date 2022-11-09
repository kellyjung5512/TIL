import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    room = int(input())
    box = list(map(int, input().split()))
    change_room = [0] * room
    for i in range(room):
        print(change_room)
        cnt = room - i
        if box[i] > 0:
            for j in range(i, room):
                if box[i] <= box[j]:
                    cnt -= 1
        change_room[i] = cnt
        cnt = 0

    print('#{} {}'.format(tc, max(change_room)))