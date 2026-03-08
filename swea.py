import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
#상하좌우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for sy in range(n):
        for sx in range(n):
            y, x = sy, sx
            current = arr[y][x]
            cnt = 1

            while True:
                found = False
                m_val = float('inf')
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if ny < 0 or ny >= n or nx < 0 or nx >= n:
                        continue

                    if current > arr[ny][nx]:
                        if m_val > arr[ny][nx]:
                            m_val = arr[ny][nx]
                            next_y, next_x = ny, nx
                            found = True
                    
                if found == True:
                    y,x = next_y, next_x
                    current = m_val
                    cnt += 1
                
                else:
                    break

            if cnt > ans:
                ans = cnt        

    print(f'#{tc} {ans}')