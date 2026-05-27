#6m,09s,74ms
# i feel so stupid this was such an easy problem lol
import sys
input = sys.stdin.readline


def main():
    num = int(input())
    if num % 2 == 0 and num > 2:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()