import sys
sys.stdin = open("input.txt")

hole, times = map(int, input().split())
equip = list(map(int, input().split()))

multitap = []

for i in range(len(equip)):
    if len(multitap) < hole:
        multitap.append(equip[i])
        continue

    elif equip[i] in multitap:
        continue

    idx_box = []
    for j in range(hole):
        if multitap[j] in equip:
            # 어떻게 할까 고민