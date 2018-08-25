import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://play.pokemonshowdown.com/")
        self.assertIn("Showdown!", driver.title)
        try:
            element = WebDriverWait(driver, 10).until(
              EC.presence_of_element_located((By.NAME, "login"))
            )
        finally:
          driver.find_element_by_name('login').click()
          user_name = driver.find_element_by_name('username')
          user_name.send_keys('bothalomew')
          user_name.send_keys(Keys.ENTER)
          try:
            element = WebDriverWait(driver, 10).until(
              EC.presence_of_element_located((By.NAME, "password"))
            )
          finally:
            password = driver.find_element_by_name("password")
            password.send_keys("botboi")
            password.send_keys(Keys.ENTER)

            time.sleep(2)

            driver.find_element_by_name("joinRoom").click()
            driver.find_element_by_name("newTop").click()

            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Format:'])[2]/following::button[1]").click()
            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Battle Spot Doubles'])[1]/following::button[1]").click()




            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='you have no pokemon lol'])[1]/following::button[1]").click()

            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Save'])[1]/following::textarea[1]").send_keys("""Celesteela @ Weakness Policy
Ability: Lightning Rod
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD / 252 Spe
Relaxed Nature
- Metronome

Celesteela @ Weakness Policy
Ability: Mold Breaker
EVs: 252 HP / 252 Atk / 252 Def / 252 SpA / 252 SpD / 252 Spe
Relaxed Nature
- Metronome


""")

            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Import/Export'])[1]/following::button[1]").click()
            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Home'])[1]/preceding::i[1]").click()

            driver.find_element_by_name('format').click()

             #Click on Metronome Battle
            driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Battle Spot Doubles'])[1]/following::button[1]").click()


            def check_if_exists_by_name(name):
              try:
                  driver.find_element_by_name(name)
              except:
                   return False
              return True

            def click_if_exists_by_name(name):
                if check_if_exists_by_name(name):
                  driver.find_element_by_name(name).click()
                return

            while True:
              #Search for battle
              driver.find_element_by_name("search").click()
              running = True
              try:
                  element = WebDriverWait(driver, 1000).until(
                    EC.presence_of_element_located((By.NAME, "openTimer"))
                  )
              finally:
                driver.find_element_by_name("openTimer").click()
                driver.find_element_by_name("timerOn").click()

                while running:

                  for i in range(0,2):
                    click_if_exists_by_name("chooseMove")
                    time.sleep(1)
                  #try:
                   # element = WebDriverWait(driver, 100).until(
                    #  EC.presence_of_element_located((By.NAME, "goToEnd"))
                    #)
                  #finally:
                   # click_if_exists_by_name("goToEnd")
                  running = not check_if_exists_by_name("closeAndMainMenu")
                driver.find_element_by_name("closeAndMainMenu").click()

          #driver.find_element_by_name('format').click()
          #driver.find_element_by_xpath("//button[@name='selectFormat']/option[value()='Metronome Battle']").click()
        #elem = driver.find_element_by_name("q")
        #elem.send_keys("pycon")
        #elem.send_keys(Keys.RETURN)
        #assert "No results found." not in driver.page_source


    def tearDown(self):
        pass
        #self.driver.close()

if __name__ == "__main__":
    unittest.main()
