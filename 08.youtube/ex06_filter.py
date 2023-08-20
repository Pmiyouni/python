from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 1. 유튜브 접속
# 2. 검색어 입력
# 3. 엔터
# 4. 필터
# 5. 조회수 클릭
# 6. 무한 스크롤
# 7. 제목 수집 

# 스크롤 후  제목데이터를 리턴하는 함수 정의
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


# 크롬 브라우저 실행
driver = webdriver.Chrome()
# 유튜브 접속
driver.get("http://www.youtube.com/")
time.sleep(2)
# 검색창 요소 접근
search_input = driver.find_element(By.CSS_SELECTOR, 'input#search')
# 검색어 입력 
search_input.send_keys("뉴진스")
# 엔터 치기
search_input.send_keys(Keys.RETURN)

time.sleep(2)

# 필터 버튼 요소 접근
filter_button=driver.find_element(By.XPATH,'//*[@id="filter-button"]')
# 필터 버튼 클릭
filter_button.click()

# 조회수 클릭
hits=driver.find_element(By.XPATH,'/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-search-filter-options-dialog-renderer/div[2]/ytd-search-filter-group-renderer[5]/ytd-search-filter-renderer[3]/a')
# 필터의 조회수는 동일한 xpath가 많아서 전체xpath로 사용
hits.click()

# 조회수 XPATH
# //*[@id="endpoint"] 상대경로 느낌
# /html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-search-filter-options-dialog-renderer/div[2]/ytd-search-filter-group-renderer[5]/ytd-search-filter-renderer[3]/a
# 전체(full)xpath는 절대경로, 조회수나 다른 필터도 전부 xpath가 동일하므로 전체xpath로 사용

#  참조)업로드 날짜 XPATH
# //*[@id="endpoint"]

scroll_fun()
time.sleep(2)

# 제목 요소 가져오기
titles = driver.find_elements(By.XPATH,'//*[@id="video-title"]')
# 제목 출력
for title in titles:
    print(title.text) #innerHTML 값  

# print("영상 갯수:",len(titles))
