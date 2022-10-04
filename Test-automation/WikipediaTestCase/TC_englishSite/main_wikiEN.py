import unittest
from selenium import webdriver
from WikipediaTestCase.TC_englishSite import page_wikiEN


class Wiki_EN(unittest.TestCase):
    # beggining
    def setUp(self):
        print("'Search Wikipedia' search box allows to search for specified data")
        self.driver = webdriver.Chrome(USER PATH TO WEBDRIVER)
        self.driver.get("https://en.wikipedia.org/wiki/Main_Page")
        self.driver.maximize_window()

    def test_main_page_matches(self):
        mainPage = page_wikiEN.MainPage(self.driver)
        assert mainPage.is_title_matches()
        print("User is present on Wikipedia main page")

    def test_type_data(self):
        mainPage = page_wikiEN.MainPage(self.driver)
        mainPage.type_data()
        currentPage = page_wikiEN.ArticlePage(self.driver)
        assert currentPage.is_article_title_matches()
        print("User is present on article about software testing")

    def test_type_data_small_letters(self):
        mainPage = page_wikiEN.MainPage(self.driver)
        mainPage.type_data_small_letters()
        currentPage = page_wikiEN.ArticlePage(self.driver)
        assert currentPage.is_article_title_matches()
        print("User is present on article about software testing")

    def test_type_data_capital_letters(self):
        mainPage = page_wikiEN.MainPage(self.driver)
        mainPage.type_data_capital_letters()
        currentPage = page_wikiEN.ArticlePage(self.driver)
        assert currentPage.is_article_title_matches()
        print("User is present on article about software testing")

    def test_print_data(self):
        mainPage = page_wikiEN.MainPage(self.driver)
        mainPage.type_data()
        currentPage = page_wikiEN.ArticlePage(self.driver)
        currentPage.print_article()


        # end
        def tearDown(self):
            self.driver.close()

        if __name__ == "__main__":
            unittest.main()
