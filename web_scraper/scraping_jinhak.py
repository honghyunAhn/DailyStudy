from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

URL = "https://ipsi.jinhak.or.kr/subList/20000000317" # 매년마다 url을 변경해야 할 수도 있습니다.
PATH = "/chromedriver.exe"

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
time.sleep(2)

select = Select(browser.find_element_by_id('sido_nm'))
select.select_by_visible_text("경기")

browser.find_element_by_id("srchbtn").click()

time.sleep(2)