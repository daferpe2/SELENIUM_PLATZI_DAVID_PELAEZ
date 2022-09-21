import csv, unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import os
import datetime

# obtener datos del día para escribir el archivo de texto
today=datetime.date.today().strftime('%Y-%m-%d')

class TestingArc(unittest.TestCase):
    # ingreser a la pagina que se busca automatizar
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(30)
        driver.get('https://www.armada.mil.co/')

    # busca la sección de noticias e ingresa pagina por pagina hasta 4 loops   
    def test_noticias_arc(self):
        driver = self.driver
        lista_noticias = []
        for i in range(4):
            not2 = driver.find_element(By.XPATH,f'//div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div/div[{i + 1}]/div[4]/span/a')
            not2.click()
            sleep(2)
            noticia = driver.find_element(By.XPATH,'//div[1]/div[2]/div/div/div/div/header/h2')
            print(noticia.text)
            lista_noticias.append(noticia)
            cuerpo = driver.find_element(By.XPATH,'//div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[3]/div/div/p')
            print(cuerpo.text)
            lista_noticias.append(cuerpo.text)
            driver.back()

        # escritura de un archivo txt con el texto resultante de la automatización
        try:
            with open(f'{today}.txt','w',encoding='utf-8') as f:
                for o in lista_noticias:
                    f.write('%s\n' % o)
                    f.write('\n\n')

        except ValueError as ve:
            print(ve)
            
        sleep(1)

      
    def tearDown(self):
        self.driver.close()
        
if __name__=='__main__':
    unittest.main(verbosity=2)
