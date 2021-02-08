# 백준 15552번
# 빠른 A+B
# 첫 줄에 테스트케이스의 개수 T가 주어진다. T는 최대 1,000,000이다.
# Python을 사용하고 있다면, input 대신 sys.stdin.readline을 사용할 수 있다.

import sys

test_case = int(input())

for _ in range(test_case):
    input_data = sys.stdin.readline().rstrip().split(' ')
    A = int(input_data[0])
    B = int(input_data[1])
    print(A + B)
