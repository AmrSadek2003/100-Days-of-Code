from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

game_url = "https://ozh.github.io/cookieclicker/"
driver.get(game_url)

flag = True
wait = WebDriverWait(driver, 10)
english_button = wait.until(EC.element_to_be_clickable((By.ID, "langSelect-EN")))
english_button.click()

cookie_button = driver.find_element(By.ID, value="bigCookie")


def num_cookies():
    num_cookies = driver.find_element(By.ID, value="cookies")
    total_cookies = num_cookies.text
    cookie_number = total_cookies.split(" ")[0]
    cookie_number = cookie_number.replace(",", "")
    return int(cookie_number)


def countdown():
    global flag
    time.sleep(300)
    flag = False
    per_second_element = driver.find_element(By.ID, value="cookiesPerSecond")
    per_second_str = per_second_element.text
    print("TIMES UP BOY")
    print(f"Total Cookies Per Second: {per_second_str}")
    driver.quit()


def find_best_option():
    available_widgets = driver.find_elements(By.CSS_SELECTOR, value=".product.unlocked.enabled .price")
    price_list = []
    for widget in available_widgets:
        price = widget.text
        if price:
            price_list.append(int(price))

    print(price_list)

    cookie_quantity = num_cookies()
    max_val = 0
    max_index = None
    for i in range(0, len(price_list)):
        if cookie_quantity > price_list[i] > max_val:
            max_val = price_list[i]
            max_index = i
    if (max_index != None):
        print(max_index)
        print(max_val)
        best_option = available_widgets[max_index]
        id_object = best_option.get_attribute("id")
        product_number = id_object.replace("productPrice", "")
        clickable_widget = driver.find_element(By.ID, value=f"product{product_number}")
        clickable_widget.click()


def activities():
    cookie_button = driver.find_element(By.ID, value="bigCookie")
    cookie_button.click()


def check_for_upgrades():
    min_widget = driver.find_element(By.ID, value='productPrice0')
    min_widget_price = int(min_widget.text.replace(",", "").strip() or "0")
    if (min_widget_price < num_cookies()):
        find_best_option()


timer_thread = threading.Thread(target=countdown)
timer_thread.start()
last_function_two_time = time.time()

while flag:
    activities()

    current_time = time.time()
    if current_time - last_function_two_time >= 5:
        check_for_upgrades()
        last_function_two_time = current_time
