from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from time import sleep


drivers = Options()
drivers.add_argument("--headless")
drivers.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(options=drivers)
# driver = webdriver.Chrome()

driver.get('https://www.qualveiculo.net/')
placas = ('ice2973', 'nns4646', 'bfq8663', 'abc1234', 'pec2013', 'mhm0058',
          'hmg0248', 'lpt4625', 'jsq7436')

for p in placas:
    sleep(3)
    driver.find_element_by_id('placa').send_keys(p)
    driver.find_element_by_id('placa').submit()
    # sleep()
    res = driver.find_element_by_id('resultado').text
    driver.find_element_by_id('placa').clear()
    print(res)
    print()

driver.close()
driver.quit()