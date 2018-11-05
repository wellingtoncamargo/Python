import os
import glob
import unittest
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from Config_Geral import PLATFORM_VERSION,time,AppPackage,AppActivity,PlatformName,DeviceName,Servidor,Cont
from appium import webdriver



class AndroidWebViewTests(unittest.TestCase):

    def setUp(self):
        app = ''#os.path.abspath(
            #    os.path.join(os.path.dirname(__file__),
            #                 'C:/Android/selendroid-test-app.apk'))
        desired_caps = {
            'app': app,
            'appPackage': AppPackage,
            'appActivity': AppActivity,
            'platformName': PlatformName,
            'platformVersion': PLATFORM_VERSION,
            'deviceName': DeviceName,
            'noReset': 'True'
        }

        self.driver = webdriver.Remote(Servidor,
                                       desired_caps)

    def test_webview(self):
        try:
            element_present = EC.presence_of_element_located((By.XPATH, './/android.widget.TextView[@text="Perto"]'))
            WebDriverWait(self.driver, time).until(element_present)
        except TimeoutException:
            print('não encontrou')

        self.driver.find_element_by_xpath('.//android.widget.TextView[@text="Perto"]').click()
        sleep(5)


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidWebViewTests)
    unittest.TextTestRunner(verbosity=2).run(suite)