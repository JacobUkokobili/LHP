# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 16:19:44 2020

@author: JACOB
"""


import pandas as pd
import requests as rq
from bs4 import BeautifulSoup as bs

html_doc = 'https://nigeriapropertycentre.com/for-rent/flats-apartments/showtype?keywords=lagos&page='

df = pd.DataFrame()

# loop through entire web pages
for page in range(1, 74):
    
    pages = rq.get(html_doc + str(page))
    data = bs(pages.text, 'html.parser')
    soup = data.find_all('div', {'class' : 'wp-block property list'})


    for each in soup:
        name = each.find(itemprop="url").text
        loaction = each.find('address').text.strip()
        price = each.select_one('.pull-sm-left').text.strip()[1:]
        features = each.find('ul').text
    
        df = df.append(pd.DataFrame({'property' : name, 
                                     'location' : loaction, 
                                     'price' : price,
                                     'features' : features}, 
                                    index = [0]), ignore_index = True)
    
    df.to_csv('data.csv', index=False)