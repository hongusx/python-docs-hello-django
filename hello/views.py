from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello world, this is my first python program running on Azure cloud!")
