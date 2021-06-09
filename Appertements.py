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
url = "https://www.immoweb.be/en/search/house-and-apartment/for-rent?countries=BE&hasTerraceOrGarden=true&minBedroomCount=2&minPrice=900&postalCodes=1000,1040,1050,1150,1160,1170,1180,1200,1560,1600,1601,1620,1630,1640,1650,1651,1652&page=1&orderBy=cheapest&card=9368954"
html = driver.get(url)
page = driver.page_source
soup = BeautifulSoup(page, features = "html")

data = {}
property_type = soup.select("h1", {"class" : "classified__title"})[0]
data["property type"] = property_type
data = pd.DataFrame([data])
print(data)

# class specificities:
#     def __init__(self):
#         self
    
#     def propertyType(self, url = str, listings = list):
        
#         driver.get(url)
#         listings = {}
        
#         property_type = soup.select(".classified__header-primary-info .classified__title").text.strip()
#         listings["property_types"] = property_type
#         print(listings)

driver.close()
