import pandas as pd

# 성적 다루는 간단한 예제
# 학번 정보

student_number=[1,2,3,4,5]

score_java=pd.Series([98,76,60,85,80], index=student_number) # index가 1~5
score_python=pd.Series([88,92,100,55,70], index=student_number)

print(score_java)
print(score_python)

# java, python 시리즈 합계
total=score_java+score_python 
print(total)
# index 끼리 각각 연산

score_js=pd.Series([30,20,10,40,50], index=[3,2,1,4,5]) 
# index 순서를 섞어도 가능
print(score_js) 

# index 값 기준으로 정렬하여 출력
print(score_js.sort_index())

# java, python, js 총합계
total=score_java+score_python+score_js
print(total)
# 순서에 관계없이 index 끼리 각각 연산

# index 기준 내림차순 정렬
print(total.sort_index(ascending=False))
# 값 기준 오름차순 정렬
print(total.sort_values())
# 값 기준 내름차순 정렬
print(total.sort_values(ascending=False))




