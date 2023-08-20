# 파이썬코드로 작성(selenium 사용안함)
#조회수 값 추출하기

# 개발자도구에서 원하는 문자를 더블클릭하여 복사해옴
aria_label="NewJeans (뉴진스) 'OMG' Official MV (Performance ver.1) 게시자: HYBE LABELS 7개월 전 3분 40초 조회수 151,250,339회"

# 파이썬은 문자열은 index로 저장되어있음

# rfind() : 매개변수로 전달한 글자의 인덱스값을 반환(뒤에서부터)(해당 변수의 제일 마지막에서 시작하여 찾음)
# find() :해당 변수의 시작시점부터 찾음(앞에서부터)

# 앞에서부터 찾으면 제목에 조회수 포함도 찾아서 안되므로 뒤에서부터 찾음(rfind 사용 )

print(aria_label.rfind("조회수"))
print(aria_label.find("조회수"))
# 조회수가 하나 밖에 없으므로 위의 두 명령어 결과가 동일


# 조회수 값의 시작 인덱스값
print(aria_label.rfind("조회수")+4)
print(aria_label[87]) 

# 조회수 값의 끝 인덱스값
print(aria_label.rfind("회"))
print(aria_label[98])

# 조회수 값만 출력
print(aria_label[87:98])

s_index=aria_label.rfind("조회수")+4
e_index=aria_label.rfind("회")
hits=aria_label[s_index:e_index]

hits=int(hits.replace(",",""))
# 쉼표를 제거 후 정수로 변환
print(hits)
print(type(hits))





