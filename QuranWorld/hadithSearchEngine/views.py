from django.shortcuts import render
from .hadithSearchEngine import *
from googletrans import Translator
import speech_recognition as sr
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
        except:
            return render(request, 'hadith.html',{'results':results,'query':''})
    if 'english' in request.GET:
        try:

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
        except:
            return render(request, 'hadith.html',{'results':results,'query':''})
    elif 'urdu' in request.GET:
        trans = Translator()
        text = query
        newQuery = trans.translate(text, dest="en" ,src="ur")
        print(newQuery.text)
        try:
            
            resultset = search(newQuery.text)
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
        except ExpectedError as e:
            return render(request, 'quran.html',{'results':results,'query':''})
