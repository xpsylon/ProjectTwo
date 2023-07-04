from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
#from django.template import loader #cuando usamos render no se necesita el loader
from .models import Question
from django.http import Http404

""" 
OLD HARCODED
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5] #en lista las preguntas por pub_date
    output = ', '.join([q.question_text for q in latest_question_list])# iteracion y creacion nueva lista a traves de comprehension list.
    return HttpResponse(output) #hard coded. No renderea a template """


""" 
OLD
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #order list by pub_date descendente(-), slicing 5
    plantilla = loader.get_template('polls/index.html')
    context = {
        'lista_ultimas_preguntas':latest_question_list,
    }
    return HttpResponse(plantilla.render(context, request))
 """

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'lista_ultimas_preguntas':latest_question_list}
    return render(request, 'polls/index.html', context)


""" 
OLD HARD CODED
def detail(request, question_id):
    return HttpResponse(f'You are looking at question {question_id}.')
 """

""" 
OLD
def detail(request, question_id):
    try:
        frage = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Esa pregunta no existe")
    return render(request, 'polls/detail.html', {'pregunta':frage})#como context va literal de diccionario (manualmente)
 """

def detail(request, question_id):
    frage = get_object_or_404(Question, id=question_id)
    return render(request, 'polls/detail.html', {'pregunta':frage})




def results(request, question_id):
    response = 'You are looking at the results of question {question_id}.'
    return HttpResponse(response.format(question_id=question_id))

def vote(request, question_id):
    return HttpResponse(f'You are voting on question {question_id}.')