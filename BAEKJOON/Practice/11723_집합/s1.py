import sys
sys.stdin = open('input.txt', 'r')

T = int(sys.stdin.readline())
S = 1 << 21

for tc in range(T):
    temp = sys.stdin.readline().split()

    if len(temp) == 2:
        cmd, x = temp[0], int(temp[1])
    else:
        cmd = temp[0]

    if cmd == 'add':
        S |= (1 << x)
    elif cmd == 'remove':
        S &= ~(1 << x)
    elif cmd == 'check':
        if S & (1 << x):
            print(1)
        else:
            print(0)
    elif cmd == 'toggle':
        if S & (1 << x):
            S ^= (1 << x)
        else:
            S |= (1 << x)
    elif cmd == 'all':
        S = (1 << 21) -1
    elif cmd == 'empty':
        S = (1 << 21)