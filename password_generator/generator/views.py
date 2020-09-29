from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    characters = list('qwertyuiopasdfghjklzxcvbnm')
    length = 10

    my_password = ''
    for x in range(length):
        my_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password':my_password})