from abc import ABC, abstractmethod
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from db import get_connection
import pandas as pd
import sqlite3


class AbstractScrapper(ABC):

    page_name = 'name not specified'
    url = 'url not specified'

    def scrap(self) -> None:
        print(f'Scrapping {self.url}')
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        articles = self.get_all_articles()
        for article in articles:
            article.update(
                {'description': self.get_article_description(article)})
        self.driver.quit()
        self.print_results(articles)
        self.insert_articles(articles)

    @abstractmethod
    def get_all_articles(self) -> None:
        pass

    @abstractmethod
    def get_article_description(self, article) -> None:
        pass

    def print_results(self, articles) -> None:
        pd.set_option('display.max_colwidth', 20)
        print(pd.DataFrame(articles).reindex(
            columns=['title', 'link', 'description']))

    def insert_articles(self, articles) -> None:
        rows = []
        for article in articles:
            rows.append((article['title'], article['link'],
                         article['description'], self.url, self.page_name))
        conn = get_connection()
        conn.executemany(
            '''INSERT INTO ARTICLES (TITLE, LINK, DESCRIPTION, PAGE_URL, PAGE_NAME) 
            VALUES (?,?,?,?,?) ON CONFLICT DO NOTHING;''', rows)
        conn.commit()
        conn.close()
