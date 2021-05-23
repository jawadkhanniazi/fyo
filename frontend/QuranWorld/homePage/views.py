from django.shortcuts import render
from .prayerTiming import *
# Create your views here.
def index(request):
    return render(request, 'index.html')


def home(request):
    timing = []
    names = ['FAJAR','SUNRISE','ZOHAR','ASR','MAGHREB','ISHA']
    timing = prayerTime()
    city1 =timing[1:7]
    city2 =timing[8:14]
    city3 =timing[15:21]
    city4 =timing[22:28]
    city5 =timing[29:35]
    city6 =timing[35:41]
    mylist1 = zip(names,city1)
    mylist2 = zip(names,city2)
    mylist3 = zip(names,city3)
    mylist4 = zip(names,city4)
    mylist5 = zip(names,city5)
    mylist6 = zip(names,city6)

    return render(request, 'base.html',{'city1':mylist1,'names':names , 'city2':mylist2,'city3':mylist3,'city4':mylist4,'city5':mylist5,'city6':mylist6 })