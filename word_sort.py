from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re

# Путь к драйверу Chrome
driver_path = 'C:\chromedriver.exe'
service = Service(driver_path)

driver = webdriver.Chrome(service=service)

# Ждем пока сайт полностью прогрузится
wait = WebDriverWait(driver, 400)

def get_num_results(word):
    try:
        driver.get('https://shonagon.ninjal.ac.jp/search_form')

        # Ищем поле для ввода и вводим текст
        input_field = wait.until(EC.presence_of_element_located((By.ID, 'query_string')))
        input_field.clear()
        input_field.send_keys(word)

        # Нажимаем Enter
        input_field.send_keys(Keys.RETURN)

        # Ждем перехода на страницу с результатами поиска
        wait.until(EC.url_changes('https://shonagon.ninjal.ac.jp/search_form'))

        # Ищем строку с количеством результатов
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        result_string = soup.find('p', attrs={'data-v-1be3957e': ""}).text

        # Извлекаем число результатов
        num_results = int(re.search(r'\d+', result_string).group())
        return num_results
    except:
        return get_num_results(word)

# Читаем файл input.txt
with open('input.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Создаем файл output.txt для записи результатов

for line in lines:
    with open('output.txt', 'a', encoding='utf-8') as f:
        words = line.strip().split(',')
        words = [s.replace(" ", "") for s in words]
        words = [s.replace("*", "") for s in words]
        # Получаем число результатов для каждого слова
        word_results = [(word, get_num_results(word)) for word in words]
        # Сортируем слова по числу результатов
        sorted_words = [word for word, _ in sorted(word_results, key=lambda x: x[1], reverse=True)]
        # Записываем отсортированные слова в файл
        f.write(','.join(sorted_words) + '\n')

driver.quit()
