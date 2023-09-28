from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
s=Service("C:/Users/Gaming/Desktop/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(options=options,service=s)

driver.get('https://www.smartprix.com/tablets')
time.sleep(2)
old_height=driver.execute_script('return document.body.scrollHeight')
time.sleep(2)
i=1
while True:

    driver.find_element(by=By.XPATH,value='//*[@id="app"]/main/div[1]/div[3]/div[3]').click()
    time.sleep(2)
    new_height=driver.execute_script('return document.body.scrollHeight')
    print(old_height)
    print(new_height)
    print(i)
    i+=1
    if new_height==old_height:
        break
    old_height=new_height

html=driver.page_source
with open('tablets.html', 'w', encoding='utf-8') as f:
    f.write(html)


