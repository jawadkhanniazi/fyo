from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#from .Quran_E_pak_initial_work_file import *

def home(request):
    name ='jawad'
    a=1
    b=100
    c=a+b
    
    return render(request, 'home.html')

def test(request):
    n1_ = request.POST['n1']
    n2_ = request.POST['n2']
    n3 = n1_+n2_
    return render(request, 'test.html',{'sum':n3})