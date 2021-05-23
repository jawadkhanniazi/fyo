from django.shortcuts import render
from .hadithSearchEngine import *
# Create your views here.
def home(request):
    c= []
    query = ''
    resultset = search("ha hsk")
    CHAPTERNO = []
    CHAPTERNAME = []
    CHAININDEX = []
    HADITH = []
    results = zip(CHAPTERNO,CHAPTERNAME,CHAININDEX,HADITH,c)
    return render(request, 'hadith.html',{'results':results,'query':query})

    

def searchHadith(request):

    query = request.GET['query']
    resultset = search(query)
    c=['1','2','3','4','5','6','7','8','9',]
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
            
    results = zip(CHAPTERNO,CHAPTERNAME,CHAININDEX,HADITH,c)
    return render(request, 'hadith.html',{'results':results,'query':query})

   