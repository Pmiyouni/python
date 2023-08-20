from selenium import webdriver
from selenium.webdriver.common.by import By
import time


#크롬 브라우저 실행
driver=webdriver.Chrome()
# 접속할 주소(유튜브)
driver.get("https://www.youtube.com/")
time.sleep(2)
# 제목 요소 가져오기
title = driver.find_elements(By.XPATH,'//*[@id="video-title"]')

for title in title:
    # print(title.text) #innerHTML 값
    # print(title.tag_name) #해당 요소의 태그이름
    print(title.get_attribute("aria-label")) #해당요소의 aria-label 속성값 가져오기


