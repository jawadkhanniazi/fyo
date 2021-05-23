#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer


# In[3]:


Quran = pd.read_csv('G:\\fyp\\quran\\Dataset-Verse-by-Verse.csv')


# In[4]:


Quran.head(10)


# In[5]:


import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer


# In[6]:


EnglishTranslation = Quran['EnglishTranslation']
EnglishTranslation


# In[7]:


SurahNameEnglish = Quran['SurahNameEnglish']
#corpus_ =[]
#corpus_ = SurahNameEnglish_
#print(len(corpus_))

#string_data_ = ''
SurahNameEnglish = SurahNameEnglish.to_numpy()
#for line in new_corpus_:
    #string_data_ = string_data_ + ' \n '  + line
    #string_data = line + ' \n '  + string_data + 
print(SurahNameEnglish[1356])


# In[8]:


juz = Quran['Juz']
juz = juz.to_numpy() 
print(juz[786])


# In[9]:


OrignalArabicText = Quran['OrignalArabicText']
OrignalArabicText = OrignalArabicText.to_numpy() 
print(OrignalArabicText[44])


# In[10]:


#Quran = Quran.to_numpy()
#Quran

Q = pd.read_csv('G:\\fyp\\quran\\Arabic-Original.csv')
print('\n')
#Q.head(10)
#ayat = Q['Ayat']
ayat = Q.to_numpy() 
print(ayat[0])


# In[11]:


#Quran = Quran.to_numpy()
#Quran

urduQuran = pd.read_csv('G:\\fyp\\quran\\Urdu.csv')
print('\n')
#Q.head(10)
#ayat = Q['Ayat']
urduQuran = urduQuran.to_numpy() 
print(urduQuran[3])


# In[ ]:





# In[12]:


corpus =[]
corpus = EnglishTranslation
print(len(corpus))

string_data = ''
new_corpus = corpus.to_numpy()
for line in new_corpus:
    string_data = string_data + ' \n '  + line
    #string_data = line + ' \n '  + string_data + 
print(new_corpus)


# In[13]:


vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(new_corpus)
print(vectorizer.get_feature_names())
#['and', 'document', 'first', 'is', 'one', 'second', 'the', 'third', 'this']
print(X.shape)


# In[14]:


vector = X
df1 = pd.DataFrame(vector.toarray(), columns=vectorizer.get_feature_names())
df1


# In[15]:


import nltk

from nltk.corpus import stopwords
#print(stopwords.words('english'))
stop_words = set(stopwords.words('english'))
print((stop_words))


# In[16]:


def get_tokenized_list(doc_text):
    tokens = nltk.sent_tokenize(doc_text)
    length = len(tokens)
    return tokens


# In[17]:


# Function to remove stopwords from tokenized word list
def remove_stopwords(doc_text):
  cleaned_text = []
  for words in doc_text:
    if words not in stop_words:
      cleaned_text.append(words)
  return cleaned_text


# In[18]:


#Check for single document
tokens = get_tokenized_list(new_corpus[1])
print("WORD TOKENS:")
print(tokens)
doc_text = remove_stopwords(tokens)
print(len(doc_text))
print("\nAFTER REMOVING STOPWORDS:")
print(doc_text)


# In[19]:


doc_ = ' '.join(doc_text)
doc_


# In[20]:


cleaned_corpus = []
for doc in corpus:
  tokens = get_tokenized_list(doc)
  doc_text = remove_stopwords(tokens)
  #doc_text  = word_stemmer(doc_text)
  doc_text = ' '.join(doc_text)
  cleaned_corpus.append(doc_text)
cleaned_corpus


# In[21]:


vectorizerX = TfidfVectorizer()
vectorizerX.fit(cleaned_corpus)
doc_vector = vectorizerX.transform(cleaned_corpus)
print(vectorizerX.get_feature_names())

print(doc_vector.shape)


# In[22]:


df1 = pd.DataFrame(doc_vector.toarray(), columns=vectorizerX.get_feature_names())
df1


# In[30]:


def serach(q):
    query = q
    query = get_tokenized_list(query)
    query = remove_stopwords(query)
    query_vector = vectorizerX.transform(query)
    # calculate cosine similarities
    from sklearn.metrics.pairwise import cosine_similarity
    cosineSimilarities = cosine_similarity(doc_vector,query_vector).flatten()

    related_docs_indices = cosineSimilarities.argsort()[:-10:-1]
    #print(related_docs_indices)

    for i in related_docs_indices:
        if i<5000:
            data = [corpus[i]]
            print("\nayats realted to",query,"\t\t reffernce ayat number:",i+2,'\nsura name:',SurahNameEnglish[i+2],
                 '\t\t\t Juz:',juz[i+2])
            print('orignial ayat:\n',ayat[i-1])
            print('english translation:\n',data)
            print('urdu translation:\n',urduQuran[i-1])
        


# In[33]:


serach('marriage')

