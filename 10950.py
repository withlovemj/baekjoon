# 백준 10950번
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램 만들기
# 첫째 줄에 <테스트 케이스>의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다.


test_case = int(input())

for _ in range(test_case):
# 'i' 라는 변수 사용하지 않겠다는 의미로 '- (언더바)' 사용
    input_data = input().split(' ')
    A = int(input_data[0])
    B = int(input_data[1])
    print (A + B)
