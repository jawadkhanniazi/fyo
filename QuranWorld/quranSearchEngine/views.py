from django.shortcuts import render
from .QuranSearchEngine import *
from googletrans import Translator
import speech_recognition as sr



# Create your views here.
def searchQuery(request):

    query = request.GET['query']
    if 'vs' in request.GET:
        
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Speak Anything :")
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                print("You said : {}".format(text))
            except:
                print("Sorry could not recognize what you said")
        
        try:
            
            resultset = search(text)
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
            return render(request, 'quran.html',{'results':results,'query':text})
        except:
            return render(request, 'quran.html',{'results':results,'query':''}) 
    if 'english' in request.GET:
        
        
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
        except:
            return render(request, 'quran.html',{'results':results,'query':''})
    elif 'urdu' in request.GET:
        trans = Translator()
        text = query
        newQuery = trans.translate(text, dest="en" ,src="ur")
        print(newQuery.text)
        try:
            
            resultset = search(newQuery.text)
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
    elif 'arabic' in request.GET:
        trans = Translator()
        text = query
        newQuery = trans.translate(text, dest="en" ,src="ar")
        print(newQuery.text)
        try:
            
            resultset = search(newQuery.text)
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

