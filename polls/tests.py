# Create your tests here.
from django.test import TestCase
import datetime 
from django.utils import timezone
from .models import Question
from django.urls import reverse

class QuestionModelTest(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)
    
    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

#esta funcion externa va a ser utilizada en las funciones de la siguient Test Class
def create_question(texto_pregunta, dias):
    time = timezone.now() + datetime.timedelta(days=dias)
    return Question.objects.create(question_text=texto_pregunta, pub_date=time)

class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        #if no questions exist, an appropriate message will be displayed
        respuesta = self.client.get(reverse('polls:indice'))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, 'No polls are available.')
        self.assertQuerysetEqual(respuesta.context['lista_ultimas_preguntas'], [])
    
    def test_past_question(self):
        """ Questions with a pub_date in the past are displayed on the index page. """
        pregunta = create_question(texto_pregunta='Past question', dias=-30)
        respuesta = self.client.get(reverse('polls:indice'))
        self.assertQuerysetEqual(respuesta.context['lista_ultimas_preguntas'], [pregunta])
    
    