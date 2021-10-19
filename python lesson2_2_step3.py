import math
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

def calc(a, b):
    return(str(a+b))



try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("num1")
    x = int(x_element.text)
    y_element = browser.find_element_by_id("num2")
    y = int(y_element.text)
    y = calc(x, y)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(y)

    button = browser.find_element_by_xpath('//button[@type="submit"]')
    button.click()

    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
