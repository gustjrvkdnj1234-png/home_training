#SWEA

import sys
sys.stdin = open('input.txt', 'r')

#입력
def pascar(n):
    for i in range(n):
        for j in range(i+1):
            if j == 0 or j == i:
                lst[i][j] = 1
            else:
                lst[i][j] = lst[i-1][j-1] + lst[i-1][j]
            
            print(lst[i][j], end = ' ')
        print()

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    lst = [[0]*n for _ in range(n)]

    print(f'#{tc}')
    pascar(n)


