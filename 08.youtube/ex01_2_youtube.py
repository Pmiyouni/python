from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


#크롬 브라우저 실행
driver=webdriver.Chrome()
# 접속할 주소(유튜브)
driver.get("https://www.youtube.com/")
# 검색결과 페이지에 바로 접속
driver.get("https://www.youtube.com/results?search_query=뉴진스")
# 위 처럼 바로 접속하면 검색어 처리를 하지 않아도 됨

time.sleep(2)
# 검색창 요소 접근
search_element = driver.find_element(By.CSS_SELECTOR, 'input#search')
# input 태그 중에 id가 search인 것
# 유투브는 특이하게 id가 여러개이므로

# 검색어 입력
search_element.send_keys("뉴진스")

# 엔터치기
search_element.send_keys(Keys.RETURN)

# 검색버튼요소 접근
# btn = driver.find_element(By.CSS_SELECTOR, 'button#search-icon-legacy')
# 검색버튼 클릭
# btn.click()
time.sleep(2)

# 제목 요소 가져오기
title = driver.find_elements(By.XPATH,'//*[@id="video-title"]')

for title in title:
    print(title.text) #innerHTML 값    

time.sleep(5)
# https://www.youtube.com/results?search_query=뉴진스
# input 속성의 name인 search_query에 담아서 처리