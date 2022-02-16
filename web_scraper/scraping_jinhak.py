import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

URL = "https://ipsi.jinhak.or.kr/subList/20000000317" # 매년마다 url을 변경해야 할 수도 있습니다.
PATH = "./chromedriver.exe"

browser = webdriver.Chrome(PATH)
browser.maximize_window() 
res = requests.get(URL)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# 파일 이름
file_name = soup.find("h4", attrs={"id":"menuTitle"}).get_text()

# 1. 합불 사례 페이지로 이동
browser.get(URL)

# 2. 로그인 페이지 이동
browser.find_element_by_link_text("로그인").click()

# 3. id, pw 입력
browser.find_element_by_class_name("loginId").send_keys("anh288")
browser.find_element_by_class_name("loginPw").send_keys("Eduvil790&")

# 4. 로그인 버튼 클릭
browser.find_element_by_class_name("loginBt").click()

try: 
    elem =  WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "sido_nm"))
    )
except:
    browser.quit()

# 5. 지역 선택
sido_nm = browser.find_element_by_id("sido_nm")
for sido in sido_nm.find_elements_by_tag_name('option'):
    sido.click()
    
    # 6. 대학명 선택
    univ_nm = browser.find_element_by_id("univ_nm")
    for univ in univ_nm.find_elements_by_tag_name('option'):
        univ.click()
        
        # 7. 계열 선택
        mojip_aff = browser.find_element_by_id("mojip_aff")
        for mojip in mojip_aff.find_elements_by_tag_name('option'):
            mojip.click()
            
            # 8. 최종합불 선택
            for rlt_final in browser.find_elements_by_name("rlt_final"):
                rlt_final.click()
                browser.find_element_by_id("srchbtn").click()
                
                # 9. 페이지 선택
                page_len = len(browser.find_elements_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[4]/ul/li/a"))
                if page_len > 5:
                    for i in range(3, page_len-1):
                        page = "/html/body/div[2]/div[2]/div[2]/div/div[4]/ul/li[{}]/a".format(i)
                        browser.find_element_by_xpath(page).click()
                
print("성공")                
time.sleep(2)
