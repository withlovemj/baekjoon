# 백준 11022번
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램 만들기
# 각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력한다.

import sys
input = sys.stdin.readline

N = int(input())

for n in range(1, N +1):
    A, B = map(int, input().split())
    total = A + B
    # 각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력한다.
    # x는 테스트 케이스 번호이고 1부터 시작하며, C는 A+B이다.
    print('Case #{0}: {1} + {2} = {3}'.format(n, A, B, total))
