from abc import ABC, abstractmethod
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import pandas as pd


class AbstractScrapper(ABC):

    url = 'url not specified'

    def scrap(self) -> None:
        print(f'Scrapping {self.url}')
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        articles = self.get_all_articles()
        for article in articles:
            article.update(
                {'Description': self.get_article_description(article)})
        self.driver.quit()
        self.print_results(articles)

    @abstractmethod
    def get_all_articles(self) -> None:
        pass

    @abstractmethod
    def get_article_description(self, article) -> None:
        pass

    def print_results(self, articles) -> None:
        pd.set_option('display.max_colwidth', 20)
        print(pd.DataFrame(articles).reindex(
            columns=['Title', 'Link', 'Description']))
