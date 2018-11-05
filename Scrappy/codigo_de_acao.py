# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options


driver = webdriver.Chrome()
driver.get('http://www.guiainvest.com.br/lista-acoes/default.aspx')
try:
    element_present = EC.presence_of_element_located((By.TAG_NAME, 'td'))
    WebDriverWait(driver, 30).until(element_present)

except TimeoutException:
    print('Elemento não encontrado')
    driver.close()
    driver.quit()


def extract():
    v = 0
    for x in range(0, 20):
        for x in driver.find_elements_by_id(f'__{v}'):
            return x.text
        v+=1

def pages(x):
    p = 0
    for x in range(2, 24):
        driver.get(f'http://www.guiainvest.com.br/lista-acoes/default.aspx?listaacaopage={p}')
        p += 1


while x in range(0,25):
    print(pages(extract()))
    x = 0