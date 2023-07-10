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

    def test_future_question(self):
        """ Questions with a pub_date in the future arent displayed on the index page """
        create_question(texto_pregunta='Future question', dias=30)
        respuesta = self.client.get(reverse('polls:indice'))
        self.assertContains(respuesta, 'No polls are available.')
        self.assertQuerysetEqual(respuesta.context['lista_ultimas_preguntas'], [])

    def test_future_question_and_past_question(self):
        """ Even if past and future questions exist, just the past ones will be displayed. """
        pregunta = create_question(texto_pregunta='Past question', dias=-30)
        create_question(texto_pregunta='Future question', dias=30)
        respuesta = self.client.get(reverse('polls:indice'))
        self.assertQuerysetEqual(respuesta.context['lista_ultimas_preguntas'], [pregunta])

    def test_two_past_questions(self):
        """ The question index page may display multiple questions """
        pregunta1 = create_question(texto_pregunta='Past question 1', dias=-30)
        pregunta2 = create_question(texto_pregunta='Past question 2', dias=-5)
        respuesta = self.client.get(reverse('polls:indice'))
        self.assertQuerysetEqual(respuesta.content['lista_ultimas_preguntas'], [pregunta1, pregunta2])

#TESTS PARA EL DETAIL VIEW
class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """ the detail view of a question with a pub_date in the future
         returns a 404 not found """
        pregunta_futuro = create_question(texto_pregunta='Pregunta futura.', dias=5)
        url = reverse('polls:detalle', args=(pregunta_futuro.id))
        respuesta = self.client.get(url)
        self.assertEqual(respuesta.status_code, 404)

    def test_past_question(self):
        """ 
        The detail view of a question with a pub_date in the past
        displays the question text
        """
        pregunta_pasado = create_question(texto_pregunta='Pregunta pasado', dias=-5)
        url = reverse('polls:detalle', args=(pregunta_pasado.id))
        respuesta = self.client.get(url)
        self.assertContains(respuesta, pregunta_pasado.question_text)
        