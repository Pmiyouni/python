from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import pymysql  # pip install pymysql

# 셀레니움으로 인기급상승 주소 접속 
driver = webdriver.Chrome()
# driver.get("https://www.youtube.com/feed/trending")
driver.get("https://www.youtube.com")

# 무한스크롤 함수
def scroll():
    while True:
        before_scroll_height = driver.execute_script("return document.documentElement.scrollHeight")
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight)")
        time.sleep(2)
        after_scroll_height = driver.execute_script("return document.documentElement.scrollHeight")
        time.sleep(2)
        if before_scroll_height == after_scroll_height:
            break
    time.sleep(2)

# 무한스크롤 함수 호출
scroll()

# 제목, 조회수 텍스트 포함된 요소 선택
titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')
time.sleep(2)

# 제목, 조회수 리스트 선언 
hits_list = []
title_list = []

# 제목, 조회수 리스트 데이터 수집
for title in titles:
    # shorts 영상, YouTube 영화, 제목데이터 없는 컨텐츠 
    if title.get_attribute("aria-label") and title.text and "YouTube 영화" not in title.get_attribute("aria-label"): 
        aria_label = title.get_attribute("aria-label")
        start_index = aria_label.rfind("조회수")+4
        end_index = aria_label.rfind("회")
        hits = aria_label[start_index:end_index]
        # 조회수 값 범위에 따라 분리 
        # 조회수 없는 영상은 0으로, 조회수가 1000미만인 영상은 , 처리 생략 
        # 조회수 1,000 이상 영상
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

# MySQL Connection 연결
conn = pymysql.connect(
    host='127.0.0.1',
    user='user_python',
    password='1234',
    db='db_python',
    charset='utf8mb4')

# Connection 으로부터 Cursor 생성
cur = conn.cursor()

# SQL문 실행
sql = "insert into `table1`(title, hit) values(%s, %s);"
# 빈자리는 숫자나 문자 모두  %s로 표시, 백틱은 테이블명을 좀더 정확히 구분하기 위해
tuple_result = list(zip(title_list, hits_list)) # zip 활용하여 튜플리스트
cur.executemany(sql, tuple_result)
# executemany()를 사용해야하는데 매개변수로 sql과 튜플을 담은 리스트을 줌


# Connection 닫기
conn.commit()


# 제목 리스트에서 명사, 형용사 추출 
okt = Okt()
word_list = []
for title in title_list:
    # print("제목", title)
    for word, tag in okt.pos(title):
        # print(word, tag)
        if tag in ['Noun', 'Adjective']:
            word_list.append(word)

# 동일 단어 횟수 추출  
word_list_count = Counter(word_list)

# 워드클라우드 객체 선언 및 출력 
wc =  WordCloud(font_path = 'malgun', width=400, height=400)
result = wc.generate_from_frequencies(word_list_count)
plt.axis('off')
plt.imshow(result)
plt.show()
wc.to_file('result.png')
# 이미지파일 생성

# csv 파일로 저장
crawling_result = {
    "title": title_list,
    "hits": hits_list
}

dataFrame = pd.DataFrame(crawling_result)

dataFrame.sort_values(by=["hits"], ascending=False).to_csv("result.csv", encoding="utf-8-sig")