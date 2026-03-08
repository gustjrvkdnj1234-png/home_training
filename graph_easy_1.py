import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

# 인접행렬로 그래프를 입력받는다.

# 탐색 순서대로 출력하라.bfs

#visited 처리, print를 언제 할까.

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [False] * n

    queue = deque([0])
    visited[0] = True

    result = []

    while queue:

        current = queue.popleft()
        result.append(current)

        for node in range(n):
            if arr[current][node] == 1 and not visited[node]:
                visited[node] = True
                queue.append(node)
        
    print(f'#{tc}', *result)
