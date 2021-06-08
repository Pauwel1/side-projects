import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time
import numpy as np
import pandas as pd

driver = webdriver.Chrome()
url = "https://www.immoweb.be/nl/zoeken/huis-en-appartement/te-huur?countries=BE&minPrice=900&page=1&orderBy=relevance"
driver.get(url)

soup = BeautifulSoup(driver.page_source, "html.parser")
listings = soup.find_all('a', class_="card_title-link")
listings[:5]
