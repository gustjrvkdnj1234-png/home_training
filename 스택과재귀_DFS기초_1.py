#SWEA

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [False] * n

    def dfs(now):
        visited[now] = True
        print(now, end = ' ')

        for nxt in range(n):
            if arr[now][nxt] == 1 and not visited[nxt]:
                dfs(nxt)

    print(f'#{tc}', end = ' ')
    dfs(0)
    print()
