import unittest
from selenium import webdriver

class HomePageTests(unittest.TestCase):
  
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= 'C:/driverc/chromedriver.exe')
        driver = self.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        driver.implicitly_wait(15)
    
    def test_search_text_field(self):
        search_field = self.driver.find_element_by_id('search')
        
    def test_search_text_by_name(self):
        search_field = self.driver.find_element_by_name('q')
        
    def test_search_text_by_class_name(self):
        search_field = self.driver.find_element_by_class_name('input-text')
        
    def test_search_button_enable(self):
        button = self.driver.find_element_by_class_name('button')
    
    def test_count_of_promo_banner_images(self):
        banner_list = self.driver.find_element_by_class_name('promos')
        banners = self.driver.find_element_by_tag_name('img')
        #self.assertEqual(3, len(banners))
        
    def test_vip_promo(self):
        vip_promo = self.driver.find_element_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[4]/a/img')     
        
    def test_shopping_cart(self):
        shopping_cart_icon = self.driver.find_element_by_css_selector('div.header-minicart span.icon')        
            
    def tearDown(self):
        self.driver.quit()
  
if __name__ == "__main__":
    unittest.main(verbosity = 2)
    
print('---------------------------------------------------------')

prueba1 = """
# import time
import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner
# from selenium.webdriver.common.keys import Keys

class HelloWorld(unittest.TestCase):
    
    # prepara el entorno de la prueba
    @classmethod
    def setUpClass(cls): 
        cls.driver = webdriver.Chrome(executable_path = 'C:/driverc/chromedriver.exe')
        driver = cls.driver
        driver.implicitly_wait(10)
    
    # Acciones para que el navegador las automatice
    def test_hello_world(self):
        driver = self.driver
        driver.get("https://google.com")
        
    def test_visit_wikipedia(self):
        self.driver.get('https://wikipedia.org')
   
    # Cierre de la ventana en el navegador
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name= 'hello-world-report')) # Generar el reporte en un html

"""