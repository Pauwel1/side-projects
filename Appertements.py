import requests
import re
import bs4
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import numpy as np
import pandas as pd

driver = webdriver.Chrome()
headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}
url = "https://www.immoweb.be/nl/zoeken/huis-en-appartement/te-huur?countries=BE&hasTerraceOrGarden=true&minBedroomCount=2&minPrice=900&postalCodes=1000,1040,1050,1150,1160,1170,1180,1200,1560,1600,1601,1620,1630,1640,1650,1651,1652&orderBy=cheapest"
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

listings = {}

property_type = soup.select(".classified__header-primary-info .classified__title").text.strip()
listings["property_types"] = property_type
    
print(listings)

driver.close()
