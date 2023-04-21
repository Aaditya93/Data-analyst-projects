#!/usr/bin/env python
# coding: utf-8

# In[16]:


# import libraries 
from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime


# In[41]:


# connect to website
URL = 'https://www.amazon.in/Casio-Vintage-Digital-Grey-Watch-A158WA-1Q/dp/B000GAYQJ0/?_encoding=UTF8&pd_rd_w=Ij8sb&content-id=amzn1.sym.b5b6da36-128a-4deb-abfd-563ae12c2d96&pf_rd_p=b5b6da36-128a-4deb-abfd-563ae12c2d96&pf_rd_r=56BJFFXBAYZDQRX1NPV4&pd_rd_wg=k9agv&pd_rd_r=4cd7a94e-eb65-46f0-9b7b-c4cb5034e882&ref_=pd_gw_ci_mcx_mr_hp_atf_m'

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Safari/605.1.15"}
    
page = requests.get(URL,headers = headers)

soup1 = BeautifulSoup(page.content,"html.parser")

soup2 = BeautifulSoup(soup1.prettify(),"html.parser")

title = soup2.find(id = 'productTitle').get_text()

price = soup2.find(id = 'corePriceDisplay_desktop_feature_div').get_text()




# In[42]:


price = price.strip()[0:9]
title = title.strip()
print(price)


# In[43]:


import datetime
today = datetime.date.today()
print(today)


# In[47]:


import csv
header = ['Title','Price','Date']
data =[title,price,today]
type(data)
with open('AmazonWebScraperDataset.csv','w',newline = '',encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data )
    


# In[57]:


import pandas as pd
df = pd.read_csv(r'/Users/aadityashewale/Downloads/data analysis/AmazonWebScraperDataset.csv')
print(df)


# In[ ]:


# now appending data to csv 
with open('AmazonWebScraperDataset.csv','+a',newline = '',encoding'UTF8')as f:
    writer = csv.writer(f)
    writer.writerow(data )


# In[55]:


def check_price():
    URL = 'https://www.amazon.in/Casio-Vintage-Digital-Grey-Watch-A158WA-1Q/dp/B000GAYQJ0/?_encoding=UTF8&pd_rd_w=Ij8sb&content-id=amzn1.sym.b5b6da36-128a-4deb-abfd-563ae12c2d96&pf_rd_p=b5b6da36-128a-4deb-abfd-563ae12c2d96&pf_rd_r=56BJFFXBAYZDQRX1NPV4&pd_rd_wg=k9agv&pd_rd_r=4cd7a94e-eb65-46f0-9b7b-c4cb5034e882&ref_=pd_gw_ci_mcx_mr_hp_atf_m'

    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Safari/605.1.15"}
    
    page = requests.get(URL,headers = headers)

    soup1 = BeautifulSoup(page.content,"html.parser")

    soup2 = BeautifulSoup(soup1.prettify(),"html.parser")

    title = soup2.find(id = 'productTitle').get_text()
    
    price = soup2.find(id = 'corePriceDisplay_desktop_feature_div').get_text()
   
    price = price.strip()[1:9]
    title = title.strip()
    
    import datetime
    today = datetime.date.today()
    
    import csv
    header = ['Title','Price','Date']
    data =[title,price,today]

    with open('AmazonWebScraperDataset.csv','+a',newline = '',encoding='UTF8')as f:
        writer = csv.writer(f)
        writer.writerow(data)
    


# In[56]:


while(True):
    check_price()
    time.sleep(5)


# In[ ]:




