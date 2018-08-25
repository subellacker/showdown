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

    def check_if_exists_by_xpath(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except:
            return False
        return True

    def click_if_exists_by_name(self, name):
        if self.check_if_exists_by_name(name):
            self.driver.find_element_by_name(name).click()
    def click_if_exists_by_xpath(self, xpath):
        if self.check_if_exists_by_xpath(xpath):
            self.driver.find_element_by_xpath(xpath).click()
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
    #    self.click_if_exists_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Elo 1300+'])[1]/following::a[1]")
        self.battles_remaining=True
        self.watcher_array = []
        time.sleep(1)

    def update(self):
        driver = self.driver
        i = 1
        #battles_remaining = True
        battle_array = []
        if(self.battles_remaining):
            xpath_formatted =  "(.//*[normalize-space(text()) and normalize-space(.)='Elo 1300+'])[1]/following::a[{}]".format(i)
            next_xpath_formatted =  "(.//*[normalize-space(text()) and normalize-space(.)='Elo 1300+'])[1]/following::a[{}]".format(i+1)

            battle_url =  str(driver.find_element_by_xpath(xpath_formatted).get_attribute('href'))
            if battle_url not in battle_array:
                battle_array.append(battle_url)
                self.watcher_array.append(BattleWatcher(battle_url))
            #print(driver.find_element_by_xpath(xpath_formatted).get_attribute('href'))
            #battles_remaining = self.check_if_exists_by_xpath(next_xpath_formatted)
            self.battles_remaining = False
            i+=1
        #print(battle_array)
        for i in self.watcher_array:
            i.update()




       # i = 1
       # battles_remaining = True
       # while (battles_remaining):
       #     xpath_formatted =  "(.//*[normalize-space(text()) and normalize-space(.)='Elo 1300+'])[1]/following::a[{}]".format(i)
       #     next_xpath_formatted =  "(.//*[normalize-space(text()) and normalize-space(.)='Elo 1300+'])[1]/following::a[{}]".format(i+1)
       #     if xpath_formatted[-9:] not in battle_array:
       #         self.click_if_exists_by_xpath(xpath_formatted)
       #         i = 1
       #     #if not self.check_if_exists_by_xpath(xpath_formatted):

       #     time.sleep(1)
       #     self.click_if_exists_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Battles'])[1]/preceding::span[1]")

       #     time.sleep(1)
       #     battles_remaining = self.check_if_exists_by_xpath(next_xpath_formatted)
       #     i+=1
       # print(battle_array)

class BattleWatcher(ShowdownDriver):
    def __init__(self, url):
        ShowdownDriver.__init__(self, url)

    def update(self):
        if self.check_if_exists_by_name("saveReplay"):
            self.driver.find_element_by_link_text("Download replay").click()

        pass






sniffer = Sniffer("https://play.pokemonshowdown.com/")
while True:
    sniffer.update()


