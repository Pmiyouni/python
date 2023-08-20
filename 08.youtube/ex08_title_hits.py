from selenium import webdriver
from selenium.webdriver.common.by import By
import time


#크롬 브라우저 실행
driver=webdriver.Chrome()
# 접속할 주소(유튜브)
driver.get("https://www.youtube.com/")
time.sleep(2)
# 제목 요소 가져오기
titles = driver.find_elements(By.XPATH,'//*[@id="video-title"]')

for title in titles:
    if title.get_attribute("aria-label") and title.text: # shorts 영상을 걸러내기 위한 조건문 
        # aria_label 속성값가져오고 제목이 있는 것만 해당
        # shorts는 aria_label이 없으며 더보기안에서 가져오지 못하도록 제목이 있는 것만 거름

        aria_label = title.get_attribute("aria-label")
        # print(aria_label)
        s_index=aria_label.rfind("조회수")+4
        e_index=aria_label.rfind("회")
        hits=aria_label[s_index:e_index]
        hits=int(hits.replace(",",""))
        # 쉼표를 제거 후 정수로 변환
        print("제목", title.text)
        print("조회수", hits)
