# 백준 10818번: 최소, 최대
# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램 만들기

num = int(input())
num_list= list(map(int,input().split()))
num_list.sort()

print(num_list[0],num_list[num-1])
