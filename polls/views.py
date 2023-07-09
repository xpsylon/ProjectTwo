from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
#from django.template import loader #cuando usamos render no se necesita el loader
from .models import Question, Choice
from django.urls import reverse
from django.views import generic
from django.utils import timezone
""" 
OLD DUMMY DATA
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

"""
OLD. REPLACED BY GENERIC (CLASS-BASED) VIEW
 def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'lista_ultimas_preguntas':latest_question_list}
    return render(request, 'polls/index.html', context)
 """

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'lista_ultimas_preguntas'

    def get_queryset(self) -> QuerySet[Any]:
        # agregamos lookup lte (less than or equal) para que no imprima preguntas con fecha futura.
        return Question.objects.filter(pub_date__lte=timezone.now).order_by('-pub_date')[:5]

""" 
OLD DUMMY DATA
def detail(request, question_id):
    return HttpResponse(f'You are looking at question {question_id}.')
 """

""" 
OLD
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Esa pregunta no existe")
    return render(request, 'polls/detail.html', {'pregunta':question})#como context va literal de diccionario (manualmente)
 """

""" 
OLD. REPLACED BY GENERIC (CLASS-BASED) VIEW
def detail(request, question_id):
    frage = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'pregunta':frage})
 """

class DetailQuestionView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

"""
OLD
DUMMY DATA
 def results(request, question_id):
    response = 'You are looking at the results of question {question_id}.'
    return HttpResponse(response.format(question_id=question_id))
 """


""" OLD. REPLACED BY GENERIC (CLASS-BASED) VIEW
def results(request, question_id):
    frage = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'pregunta': frage}) """

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

""" 
OLD 
DUMMY DATA
def vote(request, question_id):
    return HttpResponse(f'You are voting on question {question_id}.') """

def vote(request, question_id):
    frage = get_object_or_404(Question, pk=question_id)
    try:
        opcion_elegida = frage.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'pregunta':frage, 'error_message': 'No ha seleccionado una opcion'})
    else:
        opcion_elegida.votes += 1
        opcion_elegida.save()
    return HttpResponseRedirect(reverse('polls:resultados', args=(question_id,)))
