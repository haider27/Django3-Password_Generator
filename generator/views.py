from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.
def home(request):
    return render(request , 'generator/home.html', {'password':'hfjgrjgf'})
def learn(request):
    return HttpResponse('<h1>start learning...You will succeed!</h1>')
def password(request):


    Characters = list("abcdefghijklmnopqrstuvwxyz")

    if request.GET.get('uppercase'):
        Characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        Characters.extend(list('@#$%^&*-+='))
    if request.GET.get('numbers'):
        Characters.extend(list('0123456789'))


    length=int(request.GET.get('length',12))
    thePassword=''
    for i in range(length):
        thePassword+=random.choice(Characters)
    return render(request , 'generator/password.html', {'password':thePassword})
def about(request):
    return render(request , 'generator/about.html')

def mission(request):
    return render(request , 'generator/mission.html')
