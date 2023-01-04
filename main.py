from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

url = 'https://clubedogol.com/'
chromedriver = ChromeDriverManager().install()

driver = webdriver.Chrome(chromedriver)

driver.get(url)

search_input = driver.find_element(By.ID, 'wp-block-search__input-1')
search_input.send_keys('clube do gol g3')

search_button = driver.find_element(By.XPATH, '//button[text()="Pesquisar"]')
search_button.click()

sleep(5)
driver.close()
