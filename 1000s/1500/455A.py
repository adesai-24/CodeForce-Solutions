# 24m, 52s, 87ms
# this took a while because of some small dp nuances, but kind of similar to house robber? very rusty on dp, need to do more dp problems, i got this after such a long time
import sys 
input = sys.stdin.readline


def solve():
    n = int(input())
    seq = list(map(int, input().split()))
    max_val = max(seq)
    freq = [0] * (max_val+1)
    for x in seq:
        freq[x] += 1
    dp = [0] * (max_val+31)
    if max_val >= 1:
        dp[1] = freq[1]
    for v in range(2, max_val + 1):
        take = dp[v-2] + v*freq[v]
        skip = dp[v-1]
        dp[v] = max(take, skip)
    print(dp[max_val])
        


solve()