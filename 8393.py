# 백준 8393번
# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램 만들기

sum = 0

n = int(input())

for i in range(1, n + 1):
    sum += i
    
print(sum)
