from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


url = "https://mytenge.kz/currency/zhezkazgan"
browser = webdriver.Chrome(service=Service(executable_path="chromedriver/chromedriver.exe"))

try:
    browser.get(url=url)
    course = browser.find_elements(By.CLASS_NAME, "ex-1-item-2")
    dollar = course[0].text
    euro = course[1].text
    ruble = course[2].text
    with open('currency_course.txt', 'w', encoding="utf-8") as f:
        f.write(f"{dollar}\n\r{euro}\n\r{ruble}")
except Exception as ex:
    print(ex)
finally:
    browser.close()
    browser.quit()
