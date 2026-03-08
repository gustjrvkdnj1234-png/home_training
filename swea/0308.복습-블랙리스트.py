import sys
sys.stdin = open('input.txt', 'r')

#블랙리스트 정보
#아파트에 일반 시민은 몇 명, 블랙리스트 몇명? 한 그룹은 -

t = int(input())
for tc in range(1, t+1):
    #아파트의 세로와 가로, 중복존재
    h, w = map(int, input().split())
    #아파트 만큼의 2차원 배열 주어짐
    apart = [list(map(int, input().split())) for _ in range(h)]
    #블랙리스트 정보 2차원
    a, b = map(int, input().split())
    black = [list(map(int, input().split())) for _ in range(a)]

    black_list = [0] * 1000001
    #블랙 리스트 번호 일단 확인
    for i in black:
        for j in i:
            if not black_list[j]:
                black_list[j] = 1
    #블랙리스트의 번호들이 1로 담긴 리스트가 있음
    #아파트를 전체 명 수에서 번호의 값이 1이면 블랙에 담아.
    cnt = 0
    for y in apart:
        for x in y:
            if black_list[x] == 1:
                cnt += 1

    print(f'#{tc} {cnt} {h*w - cnt}')


