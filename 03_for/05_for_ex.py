# 중첩 for문 사용 구구단 가로형, 세로형으로 각각  출력
print("range 활용")
print("가로 나열")
for i in range(2,10):   
    print(i,"단")
    for j in range(1,10):
        print(i,"*",j,"=",i*j, end=" ")
    print()

print("세로 나열")
for i in range(2,10):   
    print(i,"단")
    for j in range(1,10):
        print(i,"*",j, "=", i*j)


print()    
print("list 활용")
list1=[2,3,4,5,6,7,8,9]
list2=[1,2,3,4,5,6,7,8,9]
for i in list1:
    print(i,"단")
    for j in list2:
        print(i,"*",j, "=",i*j)

# print("zip활용")
#   => 각각 서로 곱해지므로 구구단은 출력불가능
# list1=[1,2,3,4,5,6,7,8,9]
# list2=[1,2,3,4,5,6,7,8,9]
# for i, j in zip(list1,list2):
#     print(i,"*",j, "=",i*j)