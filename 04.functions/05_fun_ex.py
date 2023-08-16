#실행하면 콘솔에서 1또는 2 입력받고 1은 세로형 구구단, 2는 가로형 구구단 출력

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
    num=int(input("메뉴를 입력하세요(1은 세로형 구구단, 2는 가로형 구구단) num=  "))
    if num ==1 :
        v_gugudan()    
        con=False
    elif num == 2:
        h_gugudan()
        con=False
    else:
        print("메뉴 선택 오류! 다시 입력하세요!")
