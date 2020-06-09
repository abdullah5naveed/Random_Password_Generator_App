from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')



def password(request):
    chars = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        chars.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('number'):
        chars.extend(list('1234567890'))
    if request.GET.get('specialchar'):
        chars.extend(list('!@#$%^&*()_'))
    length = int(request.GET.get('length'))
    passwordis = ''
    for x in range(length):
        passwordis += random.choice(chars)

    return render(request, 'generator/password.html', {'password': passwordis})


def about(request):
    return render(request, 'generator/about.html')
