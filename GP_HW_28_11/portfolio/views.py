import glob
import os

from django.shortcuts import render


def home(request):
    return render(request, 'portfolio/home.html')


def gallery(request):
    return render(request, 'portfolio/gallery.html')


def contacts(request):
    return render(request, 'portfolio/contacts.html')

