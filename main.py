from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.python.org/")
list_of_dates = []
for index in range(1, 6):
    date = driver.find_element(By.XPATH, f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{index}]/time').text
    list_of_dates.append(date)

names = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')

events = {}
for n in range(len(list_of_dates)):
    events[n] = {
        "time": list_of_dates[n],
        "name": names[n].text
    }

print(events)
input("Press Enter to quit...")

driver.quit()





