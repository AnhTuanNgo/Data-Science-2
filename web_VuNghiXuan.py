import selenium 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# read_id_pass= open("id_pass_pyan.txt")
# info= read_id_pass.readlines()
# id_infor= info[0]
# id_infor= id_infor.replace('\n','')
# pw_infor= info[1]

sleep(3)
driver = webdriver.Chrome(r"C:/chromedriver_win32/chromedriver.exe")
url="https://vunghixuan.github.io/"
# url= 'https://pyan.vn/dang-nhap'
driver.get(url)

# sleep(2)
# userName= driver.find_elements_by_name("email")
# userName[0].send_keys(id_infor)

# sleep(2)
# passWord= driver.find_elements_by_name("password")
# passWord[0].send_keys(pw_infor)

# sleep(3)
# login= driver.find_element_by_xpath('//*[@id="login"]/div/form/button')
# login.click()
