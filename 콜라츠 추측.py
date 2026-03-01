#SWEA 문제

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    cnt = 0

    #콜라츠 추측 구현
    def cola(n):
        global cnt
        if n == 1:
            return
        cnt += 1
        
        #재귀조건
        if n % 2 == 0:
            cola(n // 2)
        else:
            cola(n*3+1)

    cola(n)
    print(f'#{tc} {cnt}')