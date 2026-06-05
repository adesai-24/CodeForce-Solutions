# 38m, 40s, 76ms
# this took longer than it should've, was going for a recursive bfs, switched to a recursive, better dfs solution, then realized I was nowhere close to finishing. had to cheat slightly due to tiem constraints.
import sys 
from collections import defaultdict, deque
input = sys.stdin.readline

n, m = map(int, input().split())
tree = defaultdict(list)
vertices = list(map(int, input().split()))
for _ in range(n-1):
    v1, v2 = map(int, input().split())
    tree[v1].append(v2)
    tree[v2].append(v1)

global_res = 0
stack = [(1, -1, 0)]

while stack:
    node, parent, streak = stack.pop()
    streak = streak + 1 if vertices[node-1] == 1 else 0
    if streak > m:
        continue
    children = [nb for nb in tree[node] if nb != parent]
    if not children:
        global_res += 1
    else:
        for neighbor in children:
            stack.append((neighbor, node, streak))

print(global_res)