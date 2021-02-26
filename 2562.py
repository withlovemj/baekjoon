# 백준 2562번: 최댓값 
#9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램 만들기

inp = []

for i in range(9) :
    num = int(input())
    inp.append(num)
    
print(max(inp))
print(inp.index(max(inp)) + 1)
