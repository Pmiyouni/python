from selenium import webdriver
from selenium.webdriver.common.by import By
import time


#크롬 브라우저 실행
driver=webdriver.Chrome()
# 접속할 주소(네이버 웹툰)
driver.get("https://comic.naver.com/webtoon")

time.sleep(5)
# 로딩까지 시간?

# 웹툰 제목 접근
web_class=driver.find_elements(By.CSS_SELECTOR, '[class="ContentTitle__title_area--x24vt"]')   
# web_class=driver.find_elements_by_css_selector(".ContentTitle__title_area--x24vt")
time.sleep(2)

for c in web_class:        
    print(c.text)
