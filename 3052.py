# 백준 3052번 : 나머지 
# https://www.acmicpc.net/problem/3052

a = {}

for i in range(0,10):
    b = int(input())
    a[b%42] = i
    
print(len(a))
