# 19m,52s,93ms
# took a long time figuring out how submissions work.
import sys
input = sys.stdin.readline


def solve():
    num_list = list(map(int, input().split()))
    res = 0
    num_list.sort()
    for i in range(len(num_list)-1):
        res -= num_list[i]
    res += num_list[-1]
    print(res)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()

