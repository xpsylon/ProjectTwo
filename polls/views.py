from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h2>Hola, estas en polls/index</h2>')


