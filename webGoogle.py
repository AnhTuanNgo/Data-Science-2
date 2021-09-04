import selenium 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome(r"C:/chromedriver_win32/chromedriver.exe")
# url="https://vunghixuan.github.io/"
url= 'https://www.google.com/'
driver.get(url)
# https://www.google.com.vn/?hl=vi
print()
