import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
class ShowdownDriver:

    def __init__(self, url):
        profile = webdriver.FirefoxProfile()
        profile.set_preference('browser.download.folderList', 2) # custom location
        profile.set_preference('browser.download.manager.showWhenStarting', False)
        profile.set_preference('browser.download.dir', '/tmp')
        profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')
        self.driver = webdriver.Firefox()
        self.driver.get(url)

    def check_if_exists_by_name(self, name):
        try:
            self.driver.find_element_by_name(name)
        except:
            return False
        return True
    
    def check_if_exists_by_css_selector(self, selector):
        try:
            self.driver.find_element_by_css_selector(selector)
        except:
            return False
        return True


    def check_if_exists_by_link_text(self, link):
        try:
            self.driver.find_element_by_link_text(link)
        except:
            return False
        return True


    def check_if_exists_by_xpath(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except:
            return False
        return True

    def click_if_exists_by_name(self, name):
        if self.check_if_exists_by_name(name):
            try:
                self.driver.find_element_by_name(name).click()
            except:
                print("Failed to click")
    def click_if_exists_by_xpath(self, xpath):
        if self.check_if_exists_by_xpath(xpath):
            try:
                self.driver.find_element_by_xpath(xpath).click()
            except:
                print("Failed to click")
    def click_if_exists_by_css_selector(self, selector):
        if self.check_if_exists_by_css_selector(selector):
            try:
                self.driver.find_element_by_css_selector(selector).click()
            except:
                print("Failed to click")
   
    
    def click_when_exists_by_name(self, name):
        try:
            element = WebDriverWait(self.driver, 1000).until(
                    EC.presence_of_element_located((By.NAME, name))
                    )
        finally:
            self.driver.find_element_by_name(name).click()

    def click_when_exists_by_xpath(self, xpath):
        try:
            element = WebDriverWait(self.driver, 1000).until(
                    EC.presence_of_element_located((By.XPATH, xpath))
                    )
        finally:
            self.driver.find_element_by_xpath(xpath).click()

    def tearDown(self):
        pass
        #self.driver.close()


class Sniffer(ShowdownDriver):
    def __init__(self, url):
        ShowdownDriver.__init__(self, url)
        driver = self.driver
        assert "Showdown!" in driver.title
        self.click_when_exists_by_xpath("""(.//*[normalize-space(text()) and normalize-space(.)='Ladder'])[1]/following::button[1]""")
        self.click_when_exists_by_name( "selectFormat")
        self.click_when_exists_by_xpath( """(.//*[normalize-space(text()) and normalize-space(.)='Balanced Hackmons'])[1]/following::button[1]""")
        self.watcher_array = []
        self.battle_array = []
        time.sleep(1)

    def update(self):
        driver = self.driver
        i = 1
        battles_remaining = True
        while(battles_remaining):
            xpath_formatted =  "(.//*[normalize-space(text()) and normalize-space(.)='Elo 1300+'])[1]/following::a[{}]".format(i)
            next_xpath_formatted =  "(.//*[normalize-space(text()) and normalize-space(.)='Elo 1300+'])[1]/following::a[{}]".format(i+1)
            if self.check_if_exists_by_xpath(xpath_formatted):
                try:
                    battle_url =  str(driver.find_element_by_xpath(xpath_formatted).get_attribute('href'))
                except:
                    print("Cant get href")
            print(battle_url)
            battle_formatted = battle_url[-25:] 

            
            if battle_formatted not in self.battle_array and "battle" in battle_formatted and len(self.battle_array)<9:
                self.battle_array.append(battle_formatted)
            xpath_url =str("//a[@href='{}']").format(battle_formatted)
            print(xpath_url)
            #driver.find_element_by_xpath(xpath_url).click()
            #self.watcher_array.append(BattleWatcher(battle_url))
            #print(driver.find_element_by_xpath(xpath_formatted).get_attribute('href'))
            battles_remaining = self.check_if_exists_by_xpath(next_xpath_formatted)
            #self.battles_remaining = False
            i+=1
        print(self.battle_array)
        

        for i in self.battle_array[:]:
            xpath_url =str("//a[@href='{}']").format(i)
            self.click_if_exists_by_xpath(xpath_url)
            self.click_if_exists_by_name("goToEnd")
            
            if self.check_if_exists_by_name("saveReplay"):
                self.battle_array.remove(i)
                close_button_str = ".closebutton[value='{}']".format(i[1:])
                self.click_if_exists_by_css_selector(close_button_str)
#                driver.find_element_by_css_selector(close_button_str).click()
        self.click_when_exists_by_name("refresh")    
        


sniffer = Sniffer("https://play.pokemonshowdown.com/")
while True:
    sniffer.update()


