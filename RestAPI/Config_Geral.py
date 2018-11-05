import os
import unittest
from appium import webdriver


PLATFORM_VERSION = '5.0'
time = 60
AppPackage = 'com.pof.android'
AppActivity = ''#''md5bd0ac14fd18091a904d19e507e93cf5d.MainActivity'
PlatformName = 'Android'
DeviceName = 'device'
#app = os.path.abspath(
                #os.path.join(os.path.dirname(__file__),
                             #'C:/Android/com.takeda.app.brasil (2).apk'))
Servidor = 'http://127.0.0.1:4723/wd/hub'
Cont = 'NATIVE_APP' #'WEBVIEW_1'
pasta = './Evidencias/'

# Campos
toolbar = './/android.widget.TextView[@text="TERMOS DE USO"]'
user = 'wscamargo'
pwd = 'wscamargo'

#Login
usuario = './/android.widget.EditText[@text="CRM ou Nome e sobrenome"]'
#senha = './/android.widget.EditText[@text="Senha"]'
senha = './/android.widget.EditText[@text=""]'
nvsenha = './/android.widget.EditText[@text=""]'
cfsenha = './/android.widget.EditText[@text=""]'


#def setUp(self):
    #desired_caps = {
    #    'app': app,
    #    'appPackage': AppPackage,
    #    'appActivity': AppActivity,
    #    'platformName': PlatformName,
    #    'platformVersion': PLATFORM_VERSION,
    #    'deviceName': DeviceName
    #}
    #self.driver = webdriver.Remote(Servidor,
    #                               desired_caps)

#Test_Android_Carrossel_Bulario
    #script1 = Test_Android_Lista_Evento_Positivo.AndroidWebViewTests
    #self.driver.execute_script(script1)



       # self.driver.switch_to.context(Cont)  # ('WEBVIEW_1') #



   # def test_webview(self):
   #     try:
   #         element_present = EC.presence_of_element_located((By.XPATH, './/android.widget.TextView[@text="EVENTOS"]'))
   #         WebDriverWait(self.driver, time).until(element_present)
   #     except TimeoutException:
   #         print("Acessando o Menu Principal")
   #     self.driver.find_element_by_class_name('android.widget.Button').click()
   #     self.driver.swipe(100, 700, 100, 150) # Scroll movendo a tela para cima exp(X ini, Y ini, X fim, Y fim, temp(ms))
   #     self.driver.swipe(1000, 1450, 150, 1450, 150) # Scroll movendo o carrossel
   #     sleep(3)
   #     self.driver.find_element_by_class_name('android.widget.ImageButton').click()

    #def tearDown(self):
        #self.driver.quit()



#if __name__ == '__main__':
   # suite = unittest.TestLoader().loadTestsFromTestCase(AndroidWebViewTests)
   # unittest.TextTestRunner()#verbosity=2).run(suite)