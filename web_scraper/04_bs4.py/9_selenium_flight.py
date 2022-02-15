from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window() 

# //*[@id='contnent']/div[2]/div[div[4]/ul/li[1] xpath가 나올때까지 대기 한다 최대 10초까지
elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located(By.XPATH,"//*[@id='contnent']/div[2]/div[div[4]/ul/li[1]"))
