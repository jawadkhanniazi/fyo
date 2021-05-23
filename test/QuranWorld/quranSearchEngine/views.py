from django.shortcuts import render
from .QuranSearchEngine import *
# Create your views here.
def searchQuery(request):

    query = request.GET['query']
    try:
        
        resultset = search(query)
        c=['1','2','3','4','5','6','7','8','9',]
        JUZZ = []
        AYAT = []
        ENGLISH = []
        URDU = []
        AYATREF = []
        SURAH = []
        for i in resultset:
            if i <5000:
                AYATREF.append(i+2)
                ENGLISH.append(EnglishTranslation[i])
                URDU.append(urduQuran[i-1])
                JUZZ.append(juz[i+2])
                AYAT.append(ayat[i-1])
                SURAH.append(SurahNameEnglish[i])
        results = zip(JUZZ,AYAT,ENGLISH,URDU,AYATREF,SURAH,c)
        return render(request, 'quran.html',{'results':results,'query':query})
    except ExpectedError as e:
        return render(request, 'quran.html',{'results':results,'query':''})

def home(request):
    c= []
    query = ''
    resultset = search("sjdf sefj")
    JUZZ = []
    AYAT = []
    ENGLISH = []
    URDU = []
    AYATREF = []
    SURAH = []
    results = zip(JUZZ,AYAT,ENGLISH,URDU,AYATREF,SURAH,c)
    return render(request, 'quran.html',{'results':results,'query':query})

