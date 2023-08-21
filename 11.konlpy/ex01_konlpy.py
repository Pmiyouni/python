from konlpy.tag import Kkma
from konlpy.tag import Okt
from collections import Counter # 파이썬이 제공하여 따로 설치 안함

# Kkma 모듈 객체 선언
# kkma =Kkma() #대소문자 구분할 것

# print(kkma.morphs(u'안녕하세요 반갑습니다. 파이썬으로 크롤링하기'))
# #  최소단위로 쪼개어 보여줌
# # 소문자 u 는 한글깨지지 않게하기위해

# print(kkma.nouns(u'안녕하세요 반갑습니다. 파이썬으로 크롤링하기'))
# # 명사만 추출

# print(kkma.pos(u'안녕하세요 반갑습니다. 파이썬으로 크롤링하기'))
# 분석하여 형태를 알려줌
# 참고)http://kkma.snu.ac.kr/documents/index.jsp?doc=postag(꼬꼬마 한국어 형태소 분석기)

# Okt 모듈 객체 선언
okt=Okt()

# print(okt.morphs(u'안녕하세요 반갑습니다. 파이썬으로 크롤링하기'))
# print(okt.nouns(u'안녕하세요 반갑습니다. 파이썬으로 크롤링하기'))
# print(okt.pos(u'안녕하세요 반갑습니다. 파이썬으로 크롤링하기'))
# Kkma와 Okt는 결과상 약간의 차이 있음(Okt:파이썬을 명사로 인식)

# print(okt.normalize(u'안녕하세욬ㅋㅋㅋㅋㅋ'))
# normalize: 정규화로 맞춤법 고침

text="안녕하세요 파이썬입니다. 저는 파이썬을 배우고 있습니다. 파이썬은 너무나 재미있습니다. 안녕하세요 크롤링 재미있습니다. "

# 단어와 종류를 분리
# for word, tag in kkma.pos(text): # Kkma 이용
#     print(word,tag)
for word, tag in okt.pos(text):  # Okt 이용(pos는 분석하여 형태 알려줌)
    print(word,tag)

# Okt 이용
word_list=[]
# 명사,형용사만 따로 출력
for word, tag in okt.pos(text):
    # if tag in 'Noun': #명사만
    # if tag in 'Adjective': #형용사만       
    if tag in['Noun', 'Adjective']: # 명사,형용사
        # print(word,tag)
        word_list.append(word) # word만 추가
        # 명사, 형용사만 리스트에 저장
print(word_list)

# Counter로 text 문장 횟수 출력
print(Counter(text))

text_list=['파랑','빨강','노랑','빨강','파랑','초록','빨강']
print(Counter(text_list)) # Counter({'빨강': 3, '파랑': 2, '노랑': 1, '초록': 1})

#형태소 분석 결과를 Counter로 세어보기

print(Counter(word_list))
# Counter({'파이썬': 3, '안녕하세요': 2, '재미있습니다': 2, '입니다': 1, '저': 1, '있습니다': 1, 
# '크롤': 1, '링': 1})