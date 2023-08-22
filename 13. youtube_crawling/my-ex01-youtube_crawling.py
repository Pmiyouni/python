# 크롤링 결과 판다스로 저장하기
from wordcloud import WordCloud
from konlpy.tag import Okt
from collections import Counter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from PIL import Image
import numpy as np

import time
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False


def scroll_fun():
    while True:
    #스크롤 하기 전  높이
        h1 = driver.execute_script("return document.documentElement.scrollHeight")
    # print("첫번째 높이", h1)
    # 스크롤을 현재높이 만큼 내리기
        driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight)")
    # 영상 로딩 시간(잠시 대기)
        time.sleep(2)
    #스크롤 내린 뒤 높이 값
        h2= driver.execute_script("return document.documentElement.scrollHeight")
        # print("두번 째 높이:", h2)
    # 스크롤 전, 후 높이 비교
        if h1 == h2  :
            break

#크롬 브라우저 실행
driver=webdriver.Chrome()
# 접속할 주소(유튜브=>인기급상승 페이지 접속)
driver.get("https://www.youtube.com/feed/trending")

time.sleep(2)
# 검색창 요소 접근
# search_input = driver.find_element(By.CSS_SELECTOR, 'input#search')
# 검색어 입력 
# search_input.send_keys("예능")
# 검색 버튼 요소 접근 
# search_button = driver.find_element(By.CSS_SELECTOR, 'button#search-icon-legacy')
# 검색 버튼 클릭
# search_button.click()

# 엔터 치기
# search_input.send_keys(Keys.RETURN)

# 무한 스크롤 함수 호출
scroll_fun()   # 함수 정의를 상단에서 한 이후 제목요소 가져오기 전에 호출

# 제목 요소 가져오기
titles = driver.find_elements(By.XPATH,'//*[@id="video-title"]')

# 제목 저장을 위한 리스트
title_list=[]
title_list2=[]


# 조회수 저장을 위한 리스트
hits_list=[]

okt=Okt()
for title in titles:
    # shorts 영상, 유튜브영화, 제목데이터 없는 콘텐츠
    if title.get_attribute("aria-label") and title.text and "YouTube 영화" not in title.get_attribute("aria-label"): 
        aria_label = title.get_attribute("aria-label")
        s_index=aria_label.rfind("조회수")+4
        e_index=aria_label.rfind("회")
        hits=aria_label[s_index:e_index]
        # 조회수 값 범위에 따라 분리
        # 조회수 없는 영상은 0으로, 조회수가 1000미만인 영상은 ,처리생략
        # 조회수가 1,000이상 영상
        if "," in hits:
            hits = int(hits.replace(",",""))
        # 조회수 없는 영상 
        elif not hits:
            hits = 0
        # 조회수 1,000 미만 
        else:
            hits = int(hits)    

        # 동일한 제목 영상은 한 번만         
        if title.text not in title_list:
            title_list.append(title.text)
            hits_list.append(hits)
        for word, tag in okt.pos(title.text):    
            if tag in['Noun', 'Adjective']: # 명사,형용사       
                title_list2.append(word) # word만 추가




#같은 단어 노출 빈도
title_list_count=Counter(title_list2)

im = Image.open('heart.png') # 이미지 파일 읽어오기
mask_arr = np.array(im) # 픽셀 값 배열 형태 변환

#워드클라우드 객체 생성
wc=WordCloud(font_path='malgun', background_color='black', mask = mask_arr, colormap='prism', width=400, height=400)


#Counter로 분석한 데이터를 워드클라우드로 만들기
result=wc.generate_from_frequencies(title_list_count)


# 단어로 이루어진 리스트 생성
words = []
for word, count in title_list_count.most_common(5):
    # 상위 5개
    words.append(word)

# words = [word for word, count in title_list_count.most_common(5)]
# 위의 for문을 1줄로 요약, 작성하였음


# 횟수로 이루어진 리스트 생성 
counts = [count for word, count in title_list_count.most_common(5)]
colors=['yellow','green','cyan','pink','blue']
plt.bar(words, counts, color=colors)
# bar은 막대그래프 
plt.show()


# matplotlib로 이미지 출력하기
plt.axis('off') #x,y 축은 필요없으므로 생략
plt.imshow(result)

# 이미지 출력
plt.show()
wc.to_file('wordcloud_result2.png')


#제목, 조회수 리스트가 담긴 딕셔너리
c_result={
    "title":title_list,
    "hits": hits_list
}
result1=pd.DataFrame(c_result)
# Dataframe을 csv로 저장
# result.to_csv("./result.csv", encoding="utf-8-sig")

# 조회수 내림차순 정렬후 csv 저장
result1.sort_values(by=["hits"], ascending=False).to_csv("./result.csv", encoding="utf-8-sig")
