#SWEA

import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    n, m = input().split()
    stack = []
    for i in m:
        if stack and stack[-1] == i:
            stack.pop()
            continue
        
        stack.append(i)

    print(f'#{tc}', ''.join(stack))