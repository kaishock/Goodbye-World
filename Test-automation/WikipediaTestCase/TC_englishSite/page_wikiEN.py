from WikipediaTestCase.TC_englishSite.locator_wikiEN import *
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    def is_title_matches(self):
        return "Wikipedia, the free encyclopedia" in self.driver.title

    def type_data(self):
        element = self.driver.find_element(*MainPageLocators.SEARCH_BOX)
        element.send_keys("Software testing")
        time.sleep(2)
        element.send_keys(Keys.RETURN)
        time.sleep(3)

    def type_data_small_letters(self):
        element = self.driver.find_element(*MainPageLocators.SEARCH_BOX)
        element.send_keys("software testing")
        time.sleep(2)
        element.send_keys(Keys.RETURN)
        time.sleep(3)

    def type_data_capital_letters(self):
        element = self.driver.find_element(*MainPageLocators.SEARCH_BOX)
        element.send_keys("SOFTWARE TESTING")
        time.sleep(2)
        element.send_keys(Keys.RETURN)
        time.sleep(3)

class ArticlePage(BasePage):

    def is_article_title_matches(self):
        return "Software testing - Wikipedia" in self.driver.title

    def print_article(self):
        try:
            bodyContent = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "bodyContent"))
            )
            head = bodyContent.find_element(by=By.ID, value="mw-toc-heading")
            print(bodyContent.text)
            print("Successfully printed body content")
            print(head.text)

        finally:
            self.driver.quit()