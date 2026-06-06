# 36m, 19s, 10ms
# idk why it took such a long time for a greedy problem, i went with a dp mindset, but found out greedy is a better more optimal solution

import sys
from functools import lru_cache
input = sys.stdin.readline


def solve():
    n, k = map(int, input().split())
    num_walks = list(map(int, input().split()))

    extra = 0
    prev = k
    for i in range(n):
        added = max(0, k-prev-num_walks[i])
        num_walks[i] += added
        extra += added
        prev = num_walks[i]

    print(extra)
    print(*num_walks)

solve()        




