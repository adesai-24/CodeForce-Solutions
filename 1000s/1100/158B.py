# 25m,23s,93ms
# this wasn't bad at all, easy light greedy, just super verbose.

import sys
input = sys.stdin.readline

n = int(input())
friend_list = list(map(int, input().split()))

freq_map = {}


for num in friend_list:
    if num not in freq_map:
        freq_map[num] = 0
    freq_map[num] += 1

# print(freq_map)

if 4 in friend_list:
    res = freq_map[4]
    del(freq_map[4])
else:
    res = 0

if 3 in friend_list:
    while freq_map[3] != 0:
        if 1 in freq_map and freq_map[1] != 0:
            freq_map[1] -= 1
        res += 1
        freq_map[3] -= 1
    del(freq_map[3])

if 1 in freq_map and freq_map[1] == 0:
    del(freq_map[1])

if 2 in friend_list:
    if freq_map[2] % 2 == 0:
        res += freq_map[2] / 2
        del(freq_map[2])
    else:
        res += (freq_map[2]-1) / 2
        freq_map[2] = 1
        if 1 in freq_map:
            if freq_map[1] >= 2:
                freq_map[1] -= 2
            else:
                freq_map[1] -= 1
        res += 1

if 1 not in freq_map:
    print(int(res))
else:
    res += (freq_map[1] // 4)
    if freq_map[1] % 4 != 0:
        res += (1)
    print(int(res))
    