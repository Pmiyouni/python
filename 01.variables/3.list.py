# 나열형: list tuple range
# list 타입
int_list=[1,2,3,4]
print(int_list)
print(int_list[0])
print(int_list[2])
int_list[3]=500 
#  값이 변경됨
print(int_list)

# 문자열리스트
str_list=["hello","안녕","aaa"]
print(str_list)
print(str_list[0])
print(str_list[2])

# 혼합형(mix)리스트
mix_list=[1,"안녕",10,30,"hello"]
print(mix_list)
print(mix_list[2])
print(mix_list[4])

# 리스트 내에 리스트
list_in_list=[100,200,["내부리스트값",10],"aaa",1.234]
# 리스트 안에 리스트 설정
print(list_in_list)
print(list_in_list[2])
print(list_in_list[4])


