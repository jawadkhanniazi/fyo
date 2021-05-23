#!/usr/bin/env python
# coding: utf-8

# In[68]:


import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer


# In[69]:


Quran = pd.read_csv('G:\\fyp\\quran\\Dataset-Verse-by-Verse.csv')


# In[70]:


EnglishTranslation = Quran['EnglishTranslation']


# In[71]:


SurahNameEnglish = Quran['SurahNameEnglish']
#corpus_ =[]
#corpus_ = SurahNameEnglish_
#print(len(corpus_))

#string_data_ = ''
SurahNameEnglish = SurahNameEnglish.to_numpy()
#for line in new_corpus_:
    #string_data_ = string_data_ + ' \n '  + line
    #string_data = line + ' \n '  + string_data + 



# In[72]:


juz = Quran['Juz']
juz = juz.to_numpy() 


# In[73]:


OrignalArabicText = Quran['OrignalArabicText']
OrignalArabicText = OrignalArabicText.to_numpy() 


# In[74]:



Q = pd.read_csv('G:\\fyp\\quran\\Arabic-Original.csv')
print('\n')
#Q.head(10)
#ayat = Q['Ayat']
ayat = Q.to_numpy() 



# In[75]:


#Quran = Quran.to_numpy()
#Quran

urduQuran = pd.read_csv('G:\\fyp\\quran\\Urdu.csv')
print('\n')
#Q.head(10)
#ayat = Q['Ayat']
urduQuran = urduQuran.to_numpy() 



# In[76]:


corpus =[]
corpus = EnglishTranslation
print(len(corpus))

string_data = ''
new_corpus = corpus.to_numpy()
for line in new_corpus:
    string_data = string_data + ' \n '  + line
    #string_data = line + ' \n '  + string_data + 



# In[77]:


vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(new_corpus)
#print(vectorizer.get_feature_names())
#['and', 'document', 'first', 'is', 'one', 'second', 'the', 'third', 'this']


# In[78]:


vector = X
df1 = pd.DataFrame(vector.toarray(), columns=vectorizer.get_feature_names())


# In[79]:


import nltk

from nltk.corpus import stopwords
#print(stopwords.words('english'))
stop_words = set(stopwords.words('english'))


# In[80]:


def get_tokenized_list(doc_text):
    tokens = nltk.sent_tokenize(doc_text)
    length = len(tokens)
    return tokens


# In[81]:


# Function to remove stopwords from tokenized word list
def remove_stopwords(doc_text):
    cleaned_text = []
    for words in doc_text:
        if words not in stop_words:
            cleaned_text.append(words)
    return cleaned_text


# In[ ]:





# In[92]:


#Check for single document
tokens = get_tokenized_list(new_corpus[9])


doc_text = remove_stopwords(tokens)



# In[93]:


doc_ = ' '.join(doc_text)


# In[94]:


cleaned_corpus = []
for doc in corpus:
    tokens = get_tokenized_list(doc)
    doc_text = remove_stopwords(tokens)
  #doc_text  = word_stemmer(doc_text)
    doc_text = ' '.join(doc_text)
    cleaned_corpus.append(doc_text)


# In[95]:


vectorizerX = TfidfVectorizer()
vectorizerX.fit(cleaned_corpus)
doc_vector = vectorizerX.transform(cleaned_corpus)


# In[96]:


df1 = pd.DataFrame(doc_vector.toarray(), columns=vectorizerX.get_feature_names())


# In[97]:


def search(q):
    query = q
    query = get_tokenized_list(query)
    query = remove_stopwords(query)
    query_vector = vectorizerX.transform(query)
    # calculate cosine similarities
    from sklearn.metrics.pairwise import cosine_similarity
    cosineSimilarities = cosine_similarity(doc_vector,query_vector).flatten()

    related_docs_indices = cosineSimilarities.argsort()[:-10:-1]
    return related_docs_indices

    

