# 백준 10952번: A+B - 5
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램 

while True:
    a,b = map(int,input().split())
    if a == 0 and b == 0:
        break
    else:
        print(a+b)
