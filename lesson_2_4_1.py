from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100")
    )

    button1 = browser.find_element(By.ID, "book")
    button1.click()

    x = browser.find_element(By.ID, "input_value").text
    y = str(math.log(abs(12*math.sin(int(x)))))

    input1 = browser.find_element(By.ID,"answer")
    input1.send_keys(y)

    # Отправляем заполненную форму
    button2 = browser.find_element(By.ID,"solve")
    button2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
