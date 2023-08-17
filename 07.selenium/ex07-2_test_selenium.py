from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


#크롬 브라우저 실행
driver=webdriver.Chrome()
# 접속할 주소(네이버 웹툰)
driver.get("https://www.naver.com")
search_element = driver.find_element(By.XPATH, '//*[@id="query"]')
search_element.send_keys("네이버 웹툰")
search_element.send_keys(Keys.RETURN)
# btn = driver.find_element(By.XPATH, '//*[@id="search-btn"]')
# btn.click()
time.sleep(2)


# 웹툰 제목 ,소제목 접근
web_class=driver.find_elements(By.CSS_SELECTOR, '[class="name line_2"]')  
web_class2=driver.find_elements(By.CSS_SELECTOR, '[class="sub_text"]') 


cnt=0
for wt in web_class:    
    print(wt.text, end="\t")
    print(web_class2[cnt].text)    
    cnt=cnt+1

