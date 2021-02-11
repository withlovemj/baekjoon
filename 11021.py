# 백준 11021번: A+B - 7
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램 만들기

t = int(input())

for i in range(1, t+1):   #1부터 t까지
    a, b = map(int,input().split())
    print(f'Case #{i}: {a+b}')
