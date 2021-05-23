#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests 
from bs4 import BeautifulSoup


# In[2]:


url = 'https://www.dawn.com/prayers-timings/'


# In[3]:


r = requests.get(url)
htmlContent = r.content


# In[8]:


soup = BeautifulSoup(htmlContent, 'html.parser')
#print(soup.prettify)


# In[10]:


body = soup.body


# In[24]:


paras = soup.find_all('td')
print(paras)


# In[31]:


def prayerTime():
    for text in paras:
        print(text.get_text())
    


# In[32]:


prayerTime()


# In[ ]:




