# 14m, 21s, 38ms
# i think i found an easier format for codeforce submissions (took the longest time getting to know stdin)
import sys
input = sys.stdin.readline

def solve():
    _, h = map(int, input().split())
    a = list(map(int, input().split()))
    res = 0
    for num in a:
        if num <= h:
            res += 1
        else:
            res += 2
    print(res)
    # return res

solve()

