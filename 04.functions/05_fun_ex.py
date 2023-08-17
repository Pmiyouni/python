# 실행하면 콘솔에서 1또는 2 입력받고 1은 세로형 구구단, 2는 가로형 구구단 출력
# 구구단은 각각 함수로 정의하도록한다

def v_gugudan():
    for i in range(2,10):
        print(i,"단")
        for j in range(1,10):
            print(i,"x",j,"=",i*j)


def h_gugudan():
    for i in range(2,10):
        print(i,"단")
        for j in range(1,10):
            print(i,"x",j,"=",i*j, end=" ")          
        print()


con=True
while con:
    num=int(input("메뉴를 입력하세요(1은 세로형 구구단, 2는 가로형 구구단, 0 종료) num=  "))
    if num == 1 :
        print("1선택-세로형 구구단")
        v_gugudan()      
    elif num == 2:
        print("2선택-가로형 구구단")
        h_gugudan()       
    elif num == 0:
        print("종료")         
        con=False
    else:
        print("메뉴 선택 오류! 다시 입력하세요!")





