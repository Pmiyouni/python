# 구구단 함수를 ex03_function.py에 각각 정의
# main에서 1,2 번 받아 세로형, 기로형 각각 출력

from ex03_function import *


run=True
while run:
    num=int(input("메뉴를 선택하세요(0종료) 메뉴번호:  "))
    if num == 1:
        v_gugudan()
        # ex03_function().v_gugudan()
        
    elif num == 2 :
        h_gugudan()
        
    elif num == 0 :
        print("종료") 
        run=False
    else:
        print("선택오류 다시 선택!!")




