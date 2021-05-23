#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests 
from bs4 import BeautifulSoup
url = 'https://www.dawn.com/prayers-timings/'
r = requests.get(url)
htmlContent = r.content


# In[2]:


soup = BeautifulSoup(htmlContent, 'html.parser')
paras = soup.find_all('td')


# In[3]:


list= []
def prayerTime():
    paras = soup.find_all('td')
    for x in paras:
        list.append(x.get_text())
    return list


# In[26]:


#timing = []
#timing = prayerTime()
#city1 =timing[0:7]
#city2 =timing[7:14]
#city3 =timing[14:21]
#city4 =timing[21:28]
#city5 =timing[28:35]
#city6 =timing[35:42]
#for x in city6:
    #print(x)


# In[ ]:





# In[ ]:




