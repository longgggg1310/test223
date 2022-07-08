import pickle
import selenium.webdriver 
import time
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from fake_useragent import UserAgent

from selenium.webdriver.common.by import By
from selenium import webdriver
useragent = UserAgent()
BROWSER_EXE = "C:/Program Files/Mozilla Firefox/firefox.exe"
GECKODRIVER = "C:/Users/Admin/Desktop/gecko/geckodriver.exe"
FIREFOX_BINARY = FirefoxBinary(BROWSER_EXE)
                # webdriver setting
PROFILE = webdriver.FirefoxProfile()
PROFILE.set_preference("general.useragent.override", useragent.random)

PROFILE.set_preference("dom.webnotifications.enabled", False)
PROFILE.set_preference("app.update.enabled", False)
driver = webdriver.Firefox(executable_path=GECKODRIVER,
                                        firefox_binary=FIREFOX_BINARY,
                                        firefox_profile=PROFILE
                                        )
driver.get("https://zalo.me/pc")

login1 =driver.find_element(By.CLASS_NAME,'btnLogin')
login1.click()
time.sleep(3)
login2 = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[2]/div[1]/ul/li[2]")
time.sleep(3)
login2.click()



userEle =driver.find_element(By.ID,'input-phone')

userEle.send_keys('0397229040')
time.sleep(2)
passEle = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[2]/div[2]/div/div/div/div[2]/input')
passEle.send_keys('binhminh123')
time.sleep(2)
loginEle = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[2]/div[2]/div/div/div/div[4]/a')
time.sleep(2)
loginEle.click()
time.sleep(15)

pickle.dump( driver.get_cookies() , open("cookies1.pkl","wb"))