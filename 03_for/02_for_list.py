list1=[10,20,30,40,50]
for i in list1:
    print(i)

list2=["가","나","다","라","마"]
for i in list2:
    print(i)    

list3=["python","java","c",["javascript","typescript"]]
for i in list3:
    print(i)

#리스트 2개를 동시에 반복문으로 접근하기
print("zip 활용")
for i,j in zip(list1,list2):
    print(i,j)

# 한줄로 표현할때(기본은 줄이 바뀜)
for i in list3:
    # print(i, end="  ") 공백만큼 띄기
    print(i, end="\t")
    
print()

list4=[[1,"A"],[2,"B"],[3,"C"]]
for i,j in list4:
    print(i,j)


                        
                       