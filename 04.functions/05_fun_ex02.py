def v_gugudan(i,j):
   print(i,"x",j,"=",i*j)


def h_gugudan(i,j):
    print(i,"x",j,"=",i*j, end=" ")  



num=int(input("메뉴를 입력하세요(1은 세로형 구구단, 2는 가로형 구구단) num=  "))
if num == 1 or num == 2 :  
    for i in range(2,10):
        print(i,"단")
        for j in range(1,10):
            if num ==1 :
                v_gugudan(i,j)    
            else:
                h_gugudan(i,j)
        print()        
else:
    print("메뉴 선택 오류!!")
            

        
