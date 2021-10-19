from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element_by_id("input_value")
    valuex = x_element.text
    y = calc(valuex)
    
    input1 = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    input1.send_keys(y)
    
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    
    option1 = browser.find_element_by_id("robotsRule")
    option1.click()
    
    button = browser.find_element_by_xpath('//button[@type="submit"]')
    button.click()


    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
