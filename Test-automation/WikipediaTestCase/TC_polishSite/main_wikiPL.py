import unittest
from selenium import webdriver
from WikipediaTestCase.TC_polishSite import page_wikiPL


class Wiki_PL(unittest.TestCase):
    # beggining
    def setUp(self):
        print("Rozpoczęcie Testu - pole 'Przeszukaj Wikipedię' pozwala na wyszukanie wskazanego hasła")
        self.driver = webdriver.Chrome(USER PATH TO WEBDRIVER)
        self.driver.get("https://pl.wikipedia.org/")
        self.driver.maximize_window()

    def test_main_page_matches(self):
        mainPage = page_wikiPL.MainPage(self.driver)
        assert mainPage.is_title_matches()
        print("Użytkownik znajduje się na stronie głównej Wikipedii")

    def test_type_data(self):
        mainPage = page_wikiPL.MainPage(self.driver)
        mainPage.type_data()
        currentPage = page_wikiPL.ArticlePage(self.driver)
        assert currentPage.is_article_title_matches()
        print("Użytkownik znajduje się na stronie artykułu o testowaniu oprogramowania")

    def test_type_data_small_letters(self):
        mainPage = page_wikiPL.MainPage(self.driver)
        mainPage.type_data_small_letters()
        currentPage = page_wikiPL.ArticlePage(self.driver)
        assert currentPage.is_article_title_matches()
        print("Użytkownik znajduje się na stronie artykułu o testowaniu oprogramowania")

    def test_type_data_capital_letters(self):
        mainPage = page_wikiPL.MainPage(self.driver)
        mainPage.type_data_capital_letters()
        currentPage = page_wikiPL.ArticlePage(self.driver)
        assert currentPage.is_article_title_matches()
        print("Użytkownik znajduje się na stronie artykułu o testowaniu oprogramowania")

    def test_print_data(self):
        mainPage = page_wikiPL.MainPage(self.driver)
        mainPage.type_data()
        currentPage = page_wikiPL.ArticlePage(self.driver)
        currentPage.print_article()


        # end
        def tearDown(self):
            self.driver.close()

        if __name__ == "__main__":
            unittest.main()
