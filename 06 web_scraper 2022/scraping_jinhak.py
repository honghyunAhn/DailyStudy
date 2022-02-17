import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import csv

URL = "https://ipsi.jinhak.or.kr/subList/20000000317" # 매년마다 url을 변경해야 할 수도 있습니다.
PATH = "./chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.headless = True
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36")

browser = webdriver.Chrome(PATH, options=options)
browser.maximize_window() 
res = requests.get(URL)
res.raise_for_status()

# 파일 형태 지정
filename = "합불사례.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer =  csv.writer(f)

# 목차 생성
title = "No.	지역	대학	지원	시기	전형유형	계열	모집단위	모집인원	최종	예비	반영영역수(탐구수)	활용지표	수능응시조합	국수탐표	국수탐백(평균)	국수탐등 국어(등급)	수학(과목명)	수학(등급)	영어(등급)	탐구(영역)	선택1(과목명)	선택1(등급)	선택2(과목명)	선택2(등급)	한국사(등급)	제2외국어(과목명)	제2외국어(등급)".split("\t")
writer.writerow(title)

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

# 지역 선택
sido_nm = browser.find_element_by_id("sido_nm")
for sido in sido_nm.find_elements_by_tag_name('option'):
    sido.click()
    
    # 대학명 선택
    univ_nm = browser.find_element_by_id("univ_nm")
    for univ in univ_nm.find_elements_by_tag_name('option'):
        univ.click()
        
        # 계열 선택
        mojip_aff = browser.find_element_by_id("mojip_aff")
        for mojip in mojip_aff.find_elements_by_tag_name('option'):
            mojip.click()
            
            # 최종합불 선택
            for rlt_final in browser.find_elements_by_name("rlt_final"):
                browser.execute_script("arguments[0].click();", rlt_final)
                try: 
                    elem =  WebDriverWait(browser, 100).until(
                            EC.presence_of_element_located((By.ID, "srchbtn"))
                    )
                    browser.execute_script("arguments[0].click();", browser.find_element_by_id("srchbtn"))
                except TimeoutException:
                    print("지역 : ", sido.text, ", 학교: ", univ.text, ", 계열 : ", mojip.text,  " --- 타임아웃")
                    
                # 페이지 선택
                page_len = len(browser.find_elements_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[4]/ul/li/a"))
                if page_len > 4:
                    for i in range(3, page_len-1):
                        page = "/html/body/div[2]/div[2]/div[2]/div/div[4]/ul/li[{}]/a".format(i)
                        browser.find_element_by_xpath(page).click()
                        
                        # 현재의 화면에서 표를 검색
                        soup = BeautifulSoup(browser.page_source, "lxml")
                        data_rows = soup.find("table", attrs={"class":"jstbl_list01"}).find("tbody").find_all("tr")
                        # 1행씩
                        for row in data_rows:
                            columns = row.find_all("td")
                            if len(columns) <= 1: # 의미 없는 데이터는 skip
                                continue
                            # 1열씩
                            data = [column.get_text().strip() for column in columns]
                            writer.writerow(data)
print("저장완료")