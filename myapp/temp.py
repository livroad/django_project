from selenium import webdriver
import time
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

# url = 'https://qiita.com'
url = 'https://www.rakuten-sec.co.jp/ITS/V_ACT_Login.html'
driver.get(url)
time.sleep(5)
input()
test = driver.find_element(by="xpath", value="/html/body/div[1]/header/div[1]/div/div/div[2]/ul/li[5]/a")
test.click()
input('hello')
driver.quit()