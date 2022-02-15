from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

URL = "https://ipsi.jinhak.or.kr/subList/20000000317" # 매년마다 url을 변경해야 할 수도 있습니다.
PATH = "./chromedriver.exe"

browser = webdriver.Chrome(PATH)
browser.maximize_window() 

# 1. 합불 사례 페이지로 이동
browser.get(URL)

# 2. 로그인 페이지 이동
browser.find_element_by_link_text("로그인").click()

# 3. id, pw 입력
browser.find_element_by_class_name("loginId").send_keys("anh288")
browser.find_element_by_class_name("loginPw").send_keys("Eduvil790&")

# 4. 로그인 버튼 클릭
browser.find_element_by_class_name("loginBt").click()

# 5. 합불 사례 게시판이 나올때까지 대기
try:
    elem =  WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "sido_nm"))
    )
finally:
    browser.quit()
    
select = Select(browser.find_element_by_id('sido_nm'))
select.select_by_visible_text("경기")

browser.find_element_by_id("srchbtn").click()

time.sleep(2)