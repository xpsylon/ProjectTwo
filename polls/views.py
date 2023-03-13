from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h2>Hola, estas en polls/index</h2>')

def detail(request, question_id):
    return HttpResponse(f'You are looking at question {question_id}.')

def results(request, question_id):
    response = 'You are looking at the results of question {question_id}.'
    return HttpResponse(response.format(question_id=question_id))

def vote(request, question_id):
    return HttpResponse(f'You are voting on question {question_id}.')


