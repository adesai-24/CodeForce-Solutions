# 22m,3s,53ms
# took so long to figure out the math, and I still don't understand it lol
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    res = []
    for i in range(n):
        bottom = i+1
        median = 3*n-1-2*i
        top = 3*n-2*i
        res += [bottom, median, top]
    print(*res)


# 1,2,3,4,5,6
# 1,2,3
# 1,2,3,4,5,6,7,8,9

def main():
    t = int(input())
    for _ in range(t):
        solve()



if __name__ == "__main__":
    main()