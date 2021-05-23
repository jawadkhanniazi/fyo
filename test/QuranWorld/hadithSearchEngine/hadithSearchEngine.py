#!/usr/bin/env python
# coding: utf-8

# In[75]:


import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer


# In[76]:


Hadith = pd.read_csv('G:\\fyp\\hadith\\all_hadiths_clean.csv')


# In[ ]:





# In[97]:


Hadith_text = Hadith['text_en']
chapterNO = Hadith['chapter_no']
chain_index = Hadith['chain_indx']
chapter = Hadith['chapter']


# In[98]:


corpus =[]
corpus = Hadith_text
print(len(corpus))

string_data = ''
new_corpus = corpus.to_numpy()
for line in range(10):
    string_data = string_data + ' \n '  + str(line)
    #string_data = line + ' \n '  + string_data + 
#print(new_corpus)


# In[99]:


vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(new_corpus)
#print(vectorizer.get_feature_names())
#['and', 'document', 'first', 'is', 'one', 'second', 'the', 'third', 'this']


# In[ ]:





# In[100]:


import nltk

from nltk.corpus import stopwords
#print(stopwords.words('english'))
stop_words = set(stopwords.words('english'))


# In[101]:


def get_tokenized_list(doc_text):
    tokens = nltk.sent_tokenize(doc_text)
    length = len(tokens)
    return tokens


# In[102]:


# Function to remove stopwords from tokenized word list
def remove_stopwords(doc_text):
  cleaned_text = []
  for words in doc_text:
    if words not in stop_words:
      cleaned_text.append(words)
  return cleaned_text


# In[103]:


#Check for single document
tokens = get_tokenized_list(new_corpus[1])
#print("WORD TOKENS:")
#print(tokens)
doc_text = remove_stopwords(tokens)
#print(len(doc_text))
#print("\nAFTER REMOVING STOPWORDS:")


# In[104]:


doc_ = ' '.join(doc_text)


# In[105]:


cleaned_corpus = []
for doc in corpus:
  tokens = get_tokenized_list(doc)
  doc_text = remove_stopwords(tokens)
  #doc_text  = word_stemmer(doc_text)
  doc_text = ' '.join(doc_text)
  cleaned_corpus.append(doc_text)


# In[106]:


vectorizerX = TfidfVectorizer()
vectorizerX.fit(cleaned_corpus)
doc_vector = vectorizerX.transform(cleaned_corpus)
#print(vectorizerX.get_feature_names())

#print(doc_vector.shape)


# In[107]:


df1 = pd.DataFrame(doc_vector.toarray(), columns=vectorizerX.get_feature_names())


# In[109]:


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


# In[115]:


resultset = search("PUT YOUR TRUST ON ALLAH")


# In[116]:


CHAPTERNO = []
CHAPTERNAME = []
CHAININDEX = []
HADITH = []

for i in resultset:
    if i <5000:
        CHAPTERNO.append(chapterNO[i])
        CHAPTERNAME.append(chapter[i])
        CHAININDEX.append(chain_index[i])
        HADITH.append(corpus[i])
        

