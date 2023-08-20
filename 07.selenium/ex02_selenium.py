from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#크롬 브라우저 실행
driver=webdriver.Chrome()
# 접속할 주소
driver.get("https://www.example.com")

# p 태그 요소만 접근하기
# p_element=driver.find_element(By.TAG_NAME, 'p')
# print(p_element)
# find_element는 p 태그의  첫번째요소만 가져옴
# print(type(p_element))
# print(p_element.text)

p_elements=driver.find_elements(By.TAG_NAME, 'p')
print(type(p_elements))
# find_elements는 파이썬의 리스트 형식 (모든 p태그 가져옴)
for p in p_elements:
    print(p.text)


# 10초동안 현재상태에서 대기
# time.sleep(10)
