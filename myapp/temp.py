from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

# url = 'https://qiita.com'
url = 'https://www.rakuten-sec.co.jp/ITS/V_ACT_Login.html'
driver.get(url)

wait = WebDriverWait(driver, 10)

uid_elem = wait.until(EC.presence_of_all_elements_located((By.XPATH, "/html/body/div[2]/div/div[2]/div[1]/div[1]/div/form/div/div[1]/input[1]")))
uid_elem[0].send_keys('ARHW9446')
test = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[1]/div[1]/div/form/div/div[1]/input[2]")
print(test,"test")
test.send_keys('79RewUGfX@azzxC')
test = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[1]/div[1]/div/form/ul/li[1]/button")
test.click()

test = wait.until(EC.presence_of_all_elements_located((By.XPATH, "/html/body/div[1]/div[2]/main/form[2]/div[2]/div[1]/div[1]/div[3]/div[3]/span[1]/p")))
print(test[0].text)
test = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/main/form[2]/div[2]/div[1]/div[1]/div[3]/div[3]/span[2]/p")
print(test.text)

input('hello')


driver.quit()