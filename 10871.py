# 백준 10871번: X보다 작은 수
# A에서 X보다 작은 수를 모두 출력하는 프로그램 만들기


input_data = input().split(' ')
n = int(input_data[0])
x = int(input_data[1])

a = list(map(int, input().split(' ')))

for i in a:
    if x > i:
        print(i)
