import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time


def click_with_delay(element):
    driver.execute_script("arguments[0].scrollIntoView();", element)
    time.sleep(1)  # Пауза в 1 секунду
    element.click()


def switch_to_new_tab():
    # Получить список идентификаторов всех вкладок
    all_tabs = driver.window_handles

    # Закрыть текущую (первую) вкладку
    driver.close()

    # Переключиться на новую вкладку
    new_tab = all_tabs[-1]
    driver.switch_to.window(new_tab)


def buy_it():
    print("Покупаю")
    button_all = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="InlineButtons"]//button[contains(normalize-space(.//span[@class="inline-button-text"]), "Все")]')))
    print("Нажимаю кнопку Все")
    click_with_delay(button_all)
    button_pay = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="InlineButtons"]//button[contains(normalize-space(.//span[@class="inline-button-text"]), "Оплатить")]')))
    print("Нажимаю кнопку Оплатить")
    click_with_delay(button_pay)
    time.sleep(2)
    button_rocket = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="InlineButtons"]//button[contains(normalize-space(.//span[@class="inline-button-text"]), "TON Rocket")]')))
    print("Нажимаю кнопку TON Rocket")
    click_with_delay(button_rocket)
    driver.refresh()
    button_pet_pay = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="InlineButtons"]//button[contains(normalize-space(.//span[@class="inline-button-text"]), "Оплатить")]')))
    print("Нажимаю кнопку Оплатить")
    time.sleep(2)
    click_with_delay(button_pet_pay)
    time.sleep(1)
    print("Нажимаю кнопку Перехожу по ссылке")
    driver.execute_script("window.open('https://web.tlgrm.app/#6254220235');")
    switch_to_new_tab()
    time.sleep(1)
    button_check_pay = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="InlineButtons"]//button[contains(normalize-space(.//span[@class="inline-button-text"]), "Проверить оплату")]')))
    print("Нажимаю кнопку Назад")
    click_with_delay(button_check_pay)
    button_home = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="InlineButtons"]//button[contains(normalize-space(.//span[@class="inline-button-text"]), "Домой")]')))
    print("Нажимаю кнопку Домой")
    click_with_delay(button_home)
    print("Нажимаю кнопку come to list")
    come_to_list()


def back():
    button_back = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="InlineButtons"]//button[contains(normalize-space(.//span[@class="inline-button-text"]), "Назад")]')))
    click_with_delay(button_back)


def come_to_list():
    print("Возвращаюсь к объявлениям")
    time.sleep(5)
    # Проверка наличия кнопки "P2P Обмен"
    try:
        button_p2p = wait.until(EC.presence_of_element_located((By.XPATH, '//button[contains(.//span[@class="inline-button-text"], "P2P Обмен")]')))
        click_with_delay(button_p2p)
    except TimeoutException:
        pass

    # Проверка наличия кнопки "Все объявления"
    try:
        button_all_ads = wait.until(EC.presence_of_element_located((By.XPATH, '//button[contains(.//span[@class="inline-button-text"], "Все объявления")]')))
        click_with_delay(button_all_ads)
    except TimeoutException:
        pass
    print("Вы прибыли в раздел Все объявления")


def come_to_gold():
    # Проверка наличия кнопки "Золото"
    try:
        button_epic_boxes = wait.until(EC.presence_of_element_located((By.XPATH, '//button[contains(normalize-space(.//span[@class="inline-button-text"]), "Золото")]')))
        click_with_delay(button_epic_boxes)
    except TimeoutException:
        pass
    print("Вы прибыли в раздел Золото")
    scan_gold()


def come_to_common():
    # Проверка наличия кнопки "Common Box"
    try:
        button_epic_boxes = wait.until(EC.presence_of_element_located((By.XPATH, '//button[contains(normalize-space(.//span[@class="inline-button-text"]), "Common boxes")]')))
        click_with_delay(button_epic_boxes)
    except TimeoutException:
        pass
    print("Вы прибыли в раздел Common Box")
    scan_common()


def come_to_epic():
    # Проверка наличия кнопки "Epic Box"
    try:
        button_epic_boxes = wait.until(EC.presence_of_element_located((By.XPATH, '//button[contains(normalize-space(.//span[@class="inline-button-text"]), "Epic boxes")]')))
        click_with_delay(button_epic_boxes)
    except TimeoutException:
        pass
    print("Вы прибыли в раздел Epic Box")
    scan_epic()


def send_msg(text):
    TOKEN = 'your bot token'
    CHAT_ID = 'your chat id'
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    params = {'chat_id': CHAT_ID, 'text': text}
    requests.post(url, params=params)


def scan_gold():

    print("Сканирую Золото")
    try:
        buttons = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="InlineButtons"]//button[contains(normalize-space(.//span[@class="inline-button-text"]), "$PET")]')))
        # Перебрать каждую кнопку
        for button in buttons:
            try:
                text = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'inline-button-text'))).text.strip()
                parts = text.split()
                if len(parts) >= 4:
                    first_position = int(parts[0])
                    last_position = int(parts[-1])
                    if first_position < 7 and last_position > 50:
                        click_with_delay(button)
                        text = "Попытка купить " + str(last_position) + "Золота по " + str(first_position) + " $PET"
                        send_msg(text)
                        buy_it()
                    else:
                        back()
                        break
            except NoSuchElementException:
                continue
    except TimeoutException:
        pass


def scan_common():
    print("Сканирую Common Box")
    try:
        buttons = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="InlineButtons"]//button[contains(normalize-space(.//span[@class="inline-button-text"]), "$PET")]')))

        # Перебрать каждую кнопку
        for button in buttons:
            try:
                text = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'inline-button-text'))).text.strip()
                parts = text.split()
                if len(parts) >= 4:
                    first_position = int(parts[0])
                    last_position = int(parts[-1])
                    if first_position < 7 and last_position > 30:
                        click_with_delay(button)
                        text = "Попытка купить " + str(last_position) + "Common Box по " + str(first_position) + " $PET"
                        send_msg(text)
                        buy_it()
                    else:
                        back()
                        break
            except NoSuchElementException:
                continue
    except TimeoutException:
        pass


def scan_epic():
    print("Сканирую Epic Box")
    try:
        buttons = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="InlineButtons"]//button[contains(normalize-space(.//span[@class="inline-button-text"]), "$PET")]')))

        # Перебрать каждую кнопку
        for button in buttons:
            try:
                text = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'inline-button-text'))).text.strip()
                parts = text.split()
                if len(parts) >= 4:
                    first_position = int(parts[0])
                    last_position = int(parts[-1])
                    if first_position < 205 and last_position > 3:
                        click_with_delay(button)
                        text = "Попытка купить " + str(last_position) + "Epic Box по " + str(first_position) + " $PET"
                        send_msg(text)
                        buy_it()
                    else:
                        back()
                        break
            except NoSuchElementException:
                continue
    except TimeoutException:
        pass


def where_i_am():
    try:
        div_epic = driver.find_element(By.XPATH, '//div[contains(@class, "text-content") and contains(normalize-space(), "Epic boxes")]')
        div_common = driver.find_element(By.XPATH, '//div[contains(@class, "text-content") and contains(normalize-space(), "Common boxes")]')
        div_gold = driver.find_element(By.XPATH, '//div[contains(@class, "text-content") and contains(normalize-space(), "Золото")]')
        # Если хотя бы один из элементов найден, выполнить функцию back()
        back()
    except NoSuchElementException:
        # Все элементы отсутствуют, продолжить выполнение другого кода
        pass


def auth():
    driver.get(petmarketplace)
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Log in by phone Number"]')))
    click_with_delay(login_button)
    phone_input = wait.until(EC.presence_of_element_located((By.ID, 'sign-in-phone-number')))
    phone_input.send_keys('your number')
    next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"].Button.default.primary.has-ripple')))
    click_with_delay(next_button)
    verification_code = input("Введите проверочный код: ")
    code_input = wait.until(EC.presence_of_element_located((By.ID, 'sign-in-code')))
    code_input.send_keys(verification_code)
    password_input = wait.until(EC.presence_of_element_located((By.ID, 'sign-in-password')))
    password_input.send_keys('your password')
    next_button_login = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button.Button.default.primary.has-ripple')))
    click_with_delay(next_button_login)


def start():
    while 1:
        come_to_epic()
        come_to_gold()
        come_to_common()
        time.sleep(5)


if __name__ == '__main__':
    options = Options()
    options.add_argument('--headless')  # Запуск браузера в режиме без графического интерфейса
    driver_path = "../chromedriver.exe"
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver, 10)
    tonRocket = "https://web.tlgrm.app/#5014831088"
    petmarketplace = "https://web.tlgrm.app/#6254220235"
    auth()
    #where_i_am()
    start()



