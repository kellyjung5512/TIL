import sys
sys.stdin = open("input.txt")

hole, times = map(int, input().split())  # hole == 멀티탭 개수, times == 꼽아야 하는 장치의 개수
equip = list(map(int, input().split()))  # equip == 장치 리스트

multitap = []  # multitap == 멀티탭
cnt = 0

for i in range(len(equip)):
    if len(multitap) < hole:
        multitap.append(equip[i])
        continue

    elif equip[i] in multitap:
        continue

    equip_idx = 101
    out_list = []
    for j in range(hole):
        if multitap[j] in equip[i:]:
            equip_idx = equip[i:].index(multitap[j])

        out_list.append(equip_idx)

    plug_out = out_list.index(max(out_list))
    multitap.pop(plug_out)

    multitap.append(equip[i])
    cnt += 1

print(cnt)