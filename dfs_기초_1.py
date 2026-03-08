#SWEA 길찾기 - 기본

import sys
sys.stdin = open('input.txt', 'r')

def dfs(now):
    global found
    if now == 99:
        found = 1
        return
    
    visited[now] = True

    for nxt in arr[now]:
        if not visited[nxt]:
            dfs(nxt)

for _ in range(1, 11):
    tc, n = map(int, input().split())
    lst = list(map(int, input().split()))
    found = 0
    arr = [[] for _ in range(100)]
    visited = [False] * 100
    for i in range(0, len(lst), 2):
        u, v = lst[i], lst[i+1]
        arr[u].append(v)
    
    dfs(0)

    print(f'#{tc} {found}')
