import pandas as pd

# DataFrame : 2차원 구조
scores = pd.DataFrame(
    [
        [96,76,60,85,80], #java
        [88,92,100,55,70], #python
        [10,20,30,40,50] #js
    ]
)
print(scores)

scores=pd.DataFrame(
    [
        [96,76,60,85,80], #java
        [88,92,100,55,70], #python
        [10,20,30,40,50] #js
    ],
    index=["java","python","js"] # index는 스트링도 가능(꼭 숫자가 아니어도 됨)
)
print(scores)


student_namber=[1,2,3,4,5]
scores=pd.DataFrame(
    [
        [96,88,10],        
        [76,92,20],        
        [60,100,30],        
        [85,55,40],        
        [80,70,50]        
    ],
    index=student_namber
)
print(scores)

scores=pd.DataFrame(
    { # 중괄호 사용
        "java":[96,76,60,85,80], # java는 컬럼명
        "python":[88,92,100,55,70], 
        "js":[10,20,30,40,50] 
    },
    index=student_namber # 행제목
)

print(scores)

# 이름 데이터 추가
scores["이름"] = ["김파이","이파이","박파이","최파이","정파이"]
print(scores)

#데이터 추가
scores.loc[6]=[80,90,90,"조파이"]  #index 6번째 추가
print(scores)


student_namber=[1,2,3,4,5,6]
scores=pd.DataFrame(
    {
        "이름" : ["김파이","이파이","박파이","최파이","정파이","조파이"], # 이름은 컬럼명
        "java":[96,76,60,85,80,100], 
        "python":[88,92,100,55,70,20], 
        "js":[10,20,30,40,50,60] 
    },
    index=student_namber # 행제목
) # .transpose()를 )뒤에 작성하면 행열 바뀜
print(scores)

# index 기준 정렬(오름차순이 기본)
print(scores.sort_index())

# index 기준 내림차순 정렬
print(scores.sort_index(ascending=False))

# "이름" 열 기준  오름차순 정렬
print(scores.sort_values(by="이름",ascending=True))
print(scores.sort_values(by="이름",ascending=False))

#python 기준 오름차순 정렬
print(scores.sort_values(by="python",ascending=True))

# 첫 2줄 / 마지막 2줄만  조회
print(scores.head(2))
print(scores.tail(2))

# DataFrame을 csv로 내보내기
scores.to_csv("./score.csv", encoding="utf-8-sig")
# 'utf-8-sig'에서 'sig'는 'signature'의 약칭
# python을 최상위 기준으로 그 아래 생성, 한글 깨짐 방지함
# 구글 로그인하여 sheet 사용하여 확인해볼것


# 딕셔너리 데이터를 Dataframe으로 변환
# scores_dict={
#     "java":[96,76,60,85,80], # java는 컬럼명
#     "python":[88,92,100,55,70],  #python은 컬럼명
#     "js":[10,20,30,40,50] 
# }
# scores=pd.DataFrame(scores_dict)
#  print(scores_dict)
# print(scores)