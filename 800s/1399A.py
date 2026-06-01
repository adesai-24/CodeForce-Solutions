# 11m,33s,46ms
# was making a mistake with the bounds for checking, will start moving on to harder, non-greedy problems lowkey
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    n_list = list(map(int, input().split()))
    n_list.sort()
    if len(n_list) == 1:
        print("YES")
        return
    for i in range(len(n_list)):
        if i < len(n_list)-1:
            if abs(n_list[i] - n_list[i+1]) > 1:
                print("NO")
                # return "NO"
                return
    print("YES")
    # return "YES"
                


t = int(input())
for _ in range(t):
    solve()

