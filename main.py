from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

url = 'https://clubedogol.com/'
chromedriver = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=chromedriver)

driver.get(url)

search_input = driver.find_element(By.ID, 'wp-block-search__input-1')
search_input.send_keys('clube do gol g3')

search_button = driver.find_element(By.XPATH, '//button[text()="Pesquisar"]')
search_button.click()

#
#
# sleep(500)

#TODO: checar se o elemento apareceu na tela: //a[@title='Clube do Gol G3']

# driver.close()
