from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# x = driver.find_element(By.CSS_SELECTOR, "#articlecount")
#print(x.text.split()[0])

# all_portals = driver.find_element(By.LINK_TEXT, "free")
# all_portals.click()

# search_bar = driver.find_element(By.NAME, "search")
# search_bar.send_keys("python")
# search_bar.send_keys(Keys.ENTER)
driver.get("http://secure-retreat-92358.herokuapp.com/")

name = driver.find_element(By.NAME, "fName")
last_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")
submit = driver.find_element(By.CLASS_NAME, "btn")

name.send_keys("hasan")
last_name.send_keys("qadous")
email.send_keys("jefgljegl@jherlgh")
submit.click()
input("Press Enter to quit...")

driver.quit()