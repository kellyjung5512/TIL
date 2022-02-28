import sys
sys.stdin = open("input.txt")

hole, times = map(int, input().split())  # hole == 멀티탭 개수, times == 꼽아야 하는 장치의 개수
equip = list(map(int, input().split()))  # equip == 장치 리스트

multitap = []  # multitap == 멀티탭
cnt = 0

for i in range(len(equip)):
    if equip[i] in multitap:
        continue

    elif len(multitap) < hole:
        multitap.append(equip[i])
        continue

    else:
        target = []
        target_idx = []

        for m in multitap:
            if m in equip[i:]:
                target.append(m)
                target_idx.append(equip[i:].index(m))
            else:
                target.append(m)
                target_idx.append(101)
        max_idx = target_idx.index(max(target_idx))
        multitap[max_idx] = equip[i]
        cnt += 1

print(cnt)