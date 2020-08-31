from abstract.pages.soompi import Soompi
from db import db_schema

db_schema()

page = Soompi()

page.scrap()
