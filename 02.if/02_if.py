# 자바의 scanner처럼 콘솔에서 숫자 받아
# 홀수, 짝수 판별 하여 출력하는 코드 작성
num=int(input("숫자를 입력하세요 num=  "))
print("입력값:",num)
print("입력값의 타입", type(num))
if num%2 == 0:
     print("짝수")
elif num%2 != 0:     
    print("홀수")

