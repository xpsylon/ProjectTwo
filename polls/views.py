from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:2] #en lista las preguntas por pub_date
    output = ', '.join([q.question_text for q in latest_question_list])# iteracion y creacion nueva lista a traves de comprehension list.
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse(f'You are looking at question {question_id}.')

def results(request, question_id):
    response = 'You are looking at the results of question {question_id}.'
    return HttpResponse(response.format(question_id=question_id))

def vote(request, question_id):
    return HttpResponse(f'You are voting on question {question_id}.')


