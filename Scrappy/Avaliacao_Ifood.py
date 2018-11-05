# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options


class Avaliacao:
    def __init__(self, driver):
        self.driver = driver
        self.eval = 'showRating' # ID
        self.nome = 'user-name'
        self.nota = 'user-score'
        self.data = 'comment-date'
        self.coment = 'user-comment'
        self.box = 'evaluation'
        self.bt_mais = 'button load-more hide'

    def navegar(self,url):
        self.driver.get(url)
        try:
            element_present = EC.presence_of_element_located((By.CLASS_NAME, 'ab-message-button'))
            WebDriverWait(self.driver, 15).until(element_present)

        except TimeoutException:
            pass

        else:
            self.driver.find_element_by_class_name('ab-message-button').click()

         # Botão de avaliação do site

        sleep(1)
        self.driver.find_element_by_id(self.eval).click() # Botão de avaliação do site

        try:
            element_present = EC.presence_of_element_located(
                (By.CLASS_NAME, self.nome))
            WebDriverWait(self.driver, 30).until(element_present)

        except TimeoutException:
            print('Elemento não encontrado')
            self.driver.close()
            self.driver.quit()

    def __get__area(self):
        return self.driver.find_elements_by_class_name(self.box)

    def __get__nome(self, inf):
        return inf.find_element_by_class_name(self.nome)

    def __get__nota(self, inf):
        return inf.find_element_by_class_name(self.nota)

    def __get__date(self, inf):
        return inf.find_element_by_class_name(self.data)

    def __get__coment(self, inf):
        try:
            element_present = inf.find_element_by_class_name(self.coment)
            WebDriverWait(driver,1,ignored_exceptions=None).until(element_present)
        except TimeoutException:
            pass
        return inf.find_element_by_class_name(self.coment).text

    def get_all_data(self):
        avalia = self.__get__area()
        for inf in avalia:
            print(self.__get__nome(inf).text, self.__get__nota(inf).text, self.__get__date(inf).text)
            print(self.__get__coment(inf))
            print()

drivers = Options()
drivers.add_argument("--headless")
drivers.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(options=drivers) # Para executar o processo sem Browser
# driver = webdriver.Chrome() # Para acompanhar o processo pelo browser

crawl = Avaliacao(driver)
crawl.navegar('https://www.ifood.com.br/delivery/sao-paulo-sp/burger-king-cambuci')
crawl.get_all_data()


driver.quit()

