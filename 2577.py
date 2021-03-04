# 백준 2577번 : 숫자의 개수
# 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.

a = int(input())                 # 150
b = int(input())                 # 266
c = int(input())                 # 427
result = list(str(a * b * c))    # [1, 7, 0, 3, 7, 3, 0, 0]

for i in range(10):              # i = 0 ~ 9
    print(result.count(str(i)))  # i를 문자열(str)로 바꿔서 몇 개 있는지 count한다.
