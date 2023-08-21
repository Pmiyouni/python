# 크롤링 결과 판다스로 저장하기
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

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
driver.get("https://www.youtube.com/results?search_query=%EB%89%B4%EC%A7%84%EC%8A%A4")

time.sleep(2)

# 무한 스크롤 함수 호출
scroll_fun()   # 함수 정의를 상단에서 한 이후 제목요소 다져오기 전에 호출

# 제목 요소 가져오기
titles = driver.find_elements(By.XPATH,'//*[@id="video-title"]')
# 제목 저장을 위한 리스트
title_list=[]
# 조회수 저장을 위한 리스트
hits_list=[]

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

#제목, 조회수 리스트가 담긴 딕셔너리
c_result={
    "title":title_list,
    "hits": hits_list
}

result=pd.DataFrame(c_result)
# Dataframe을 csv로 저장
# result.to_csv("./result.csv", encoding="utf-8-sig")

# 조회수 내림차순 정렬후 csv 저장
result.sort_values(by=["hits"], ascending=False).to_csv("./result.csv", encoding="utf-8-sig")

