from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
from selenium.webdriver.support.select import Select
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pymysql

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

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


driver = webdriver.Chrome()
driver.get("https://www.daangn.com/hot_articles")

time.sleep(2)

# select = Select(driver.find_element(By.ID,'region1'))
# print(select)
# select.select_by_index(4)  
# select.select_by_visible_text('인천광역시')


# 무한스크롤 함수 호출
scroll()

# 제목, 관심, 채팅 포함된 요소 선택
titles = driver.find_elements(By.CLASS_NAME,'card-title')
# counts = driver.find_elements(By.CLASS_NAME,'card-counts')
prices = driver.find_elements(By.CLASS_NAME,'card-price')
jusos = driver.find_elements(By.CLASS_NAME,'card-region-name')

time.sleep(2)

# 제목, 조회수 리스트 선언 
title_list = []
price_list=[]
juso_list=[]

for title in titles:
    title_list.append(title.text)

for price in prices:   
    price_list.append(price.text)

for juso in jusos:   
    juso_list.append(juso.text)
    

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
sql = "insert into `table2`(title, price, juso) values(%s, %s, %s);"
# 빈자리는 숫자나 문자 모두  %s로 표시, 백틱은 테이블명을 좀더 정확히 구분하기 위해
tuple_result = list(zip(title_list, price_list, juso_list)) # zip 활용하여 튜플리스트
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
        if word != "판매":
        # print(word, tag)
            if tag in ['Noun']:
                word_list.append(word)

# 동일 단어 횟수 추출  
word_list_count = Counter(word_list)

im = Image.open('heart.png') # 이미지 파일 읽어오기
mask_arr = np.array(im) # 픽셀 값 배열 형태 변환

# 워드클라우드 객체 선언 및 출력 
wc=WordCloud(font_path='malgun', background_color='black', mask = mask_arr, colormap='prism', width=400, height=400)

result = wc.generate_from_frequencies(word_list_count)

# 단어로 이루어진 리스트 생성
words = []
juso_list_count = Counter(juso_list)

for word, count in juso_list_count.most_common(5):
    # 상위 5개
    words.append(word)


# 횟수로 이루어진 리스트 생성 
counts = [count for word, count in word_list_count.most_common(5)]
colors=['yellow','green','cyan','pink','blue']
plt.bar(words, counts, color=colors)
# bar은 막대그래프 
plt.show()

# matplotlib로 이미지 출력하기
plt.axis('off')
plt.imshow(result)
plt.show()
wc.to_file('result3.png')

# csv 파일로 저장
crawling_result = {
    "title": title_list,
    "price": price_list,
    "juso" : juso_list

}

dataFrame = pd.DataFrame(crawling_result)
# dataFrame.to_csv("/result3.csv", encoding="utf-8-sig")
dataFrame.sort_values(by=["juso"], ascending=False).to_csv("result3.csv", encoding="utf-8-sig")
