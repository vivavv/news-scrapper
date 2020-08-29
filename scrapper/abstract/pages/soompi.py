import requests
from ..abstract import AbstractScrapper
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
print(__name__)


class Soompi(AbstractScrapper):

    url = "https://www.soompi.com/"

    def get_all_articles(self):
        articles_soompi = []
        URL = "https://www.soompi.com/search?query=bts"
        self.driver.get(URL)
        results = self.driver.find_elements_by_css_selector(
            "h4.media-heading a")

        for result in results:
            saved = {}
            saved['Title'] = result.get_attribute('title')
            saved['Link'] = result.get_attribute('href')
            articles_soompi.append(saved)

        return articles_soompi

    def get_article_description(self, article):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(article['Link'])
        desc = driver.find_elements_by_css_selector(
            "div.article-wrapper > div p")
        return(desc[0].text)
