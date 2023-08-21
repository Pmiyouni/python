from wordcloud import WordCloud
from konlpy.tag import Okt
from collections import Counter
import matplotlib.pyplot as plt

okt=Okt()
text="안녕하세요 파이썬입니다. 저는 파이썬을 배우고 있습니다. 파이썬은 너무나 재미있습니다. 안녕하세요 크롤링 재미있습니다. "

word_list=[]
# 명사,형용사만 따로 출력
for word, tag in okt.pos(text):
    
    if tag in['Noun', 'Adjective']: # 명사,형용사       
        word_list.append(word) # word만 추가


#같은 단어 노출 빈도
word_list_count=Counter(word_list)

#워드클라우드 객체 생성
wc=WordCloud(font_path='malgun', width=400, height=400)
# 한글을 나타내기 위해 글꼴 지정 : 'malgun'은 기본글꼴

#Counter로 분석한 데이터를 워드클라우드로 만들기
result=wc.generate_from_frequencies(word_list_count)

# matplotlib로 이미지 출력하기
plt.axis('off') #x,y 축은 필요없으므로 생략

# 결과를 이미지로 출력할 준비
plt.imshow(result)

# 이미지 출력
plt.show()
