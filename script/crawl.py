from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

profile_path = r"C:\selenium_profile\cretop" 

options = webdriver.ChromeOptions()
options.add_argument(f"user-data-dir={profile_path}")

service = Service()

chrome = webdriver.Chrome(service=service, options=options)
chrome.get('https://www.cretop.com/')

_ = [x.click() for x in chrome.find_elements(By.TAG_NAME,'button')if x.text.find('닫기') >= 0]


sleep(1)
el = chrome.find_element(By.ID, 'idModel')
el.clear()
el.send_keys('NEWTALE9')

sleep(1)
el = chrome.find_element(By.ID, 'pwModel')
el.clear()
el.send_keys('whdghksdl9090!')
_ = [x.click() for x in chrome.find_elements(By.TAG_NAME,'button') if x.text == '로그인']

sleep(2)
#확인버튼 클릭
_ = [x.click() for x in chrome.find_elements(By.TAG_NAME,'button') if x.text == '확인']

#닫기버튼 클릭
chrome.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div[2]/div/div/div[1]/div/button').click()
sleep(1)

#기업으로 이동
chrome.find_element(By.XPATH, '//*[@id="app"]/div[1]/header/div/div/ul/li[1]/a/span').click()


