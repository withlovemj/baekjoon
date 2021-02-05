# 백준 2884번
# 현재 튜브가 설정한 알람 시각이 주어졌을 때, "45분 일찍 알람 설정하기" 방법을 사용한다면, 이를 언제로 고쳐야 하는지 구하는 프로그램 만들기

input_data = input().split(' ')

hour = int(input_data[0])
minute = int(input_data[1])

minute -= 45
if minute < 0:
    minute += 60
    hour -= 1
    #만약 10 10 면
    # 10 -35
    # 9 25
    if hour < 0:
        hour = 23
        
print(str(hour) + ' ' + str(minute))
