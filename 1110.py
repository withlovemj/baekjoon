# 백준 1110번: 더하기 사이클 
# 뭔말인지 1도 모르겠음,,, 그래서 https://blog.naver.com/wook2124/222086166722 참고

n = int(input())
num = n
cnt = 0

while True:
    a = num // 10
    b = num % 10
    c = (a +b) % 10
    num = (b * 10) + c
    
    cnt = cnt + 1
    if(num == n):
        break
     
print(cnt)
