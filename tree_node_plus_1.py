import sys
sys.stdin = open('input.txt', 'r')

t = int(input())
for tc in range(1, t+1):
    #n-노드개수, m-리프노드개수, l번인덱스값 출력값
    N, M, L = map(int, input().split())
    #노드 채우기 전에 트리 만들기 1부터 시작
    tree = [0]*(N+1)
    #M번 반복하면서 노드에 채우기
    for _ in range(M):
        idx, val = map(int,input().split())
        tree[idx] = val
    
    for i in range(N, 1, -1):
        parent = i // 2
        tree[parent] += tree[i]

    print(f'#{tc} {tree[L]}')