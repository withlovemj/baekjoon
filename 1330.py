# 백준 1330번
#두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램 만들기

input_data = input().split(' ')
A = int(input_data[0])
B = int(input_data[1])

if A > B:
    print('>')
elif A < B:
    print('<')
else: 
    print('==')
