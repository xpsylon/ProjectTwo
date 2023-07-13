import datetime
from django.contrib import admin
from django.db import models
from django.utils import timezone

'''In our poll app, we’ll create two models: Question and Choice. A Question has a question and a publication date. A Choice has two fields: the text of the choice and a vote tally. Each Choice is associated with a Question.
These concepts are represented by Python classes. Edit the polls/models.py file so it looks like this:'''

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('fecha publicacion')

    def __str__(self) -> str:
        return self.question_text
    
    #creamos metodo para que nos diga hace cuantos dias una pregunta fue publicada...

    """ 
    OLD WITH BUG: returns True if the pub_date is in the future
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1) """
    
    #Agregamos @decorator class-based de Django para pasar metadata al metodo was_published_recently. Viene en django.contrib.admin
    @admin.display(
        boolean=True,
        ordering='pub_date',         
        description='Published recently?',
    )

    def was_published_recently(self):
        ahora = timezone.now()
        return ahora - datetime.timedelta(days=1) <= self.pub_date <= ahora

    
    '''This is a method definition for the was_published_recently() method of a class.

This method checks whether the pub_date attribute of the object is within the last 24 hours, and returns a boolean value indicating whether it was published recently or not.

The method uses the >= operator to compare the pub_date attribute of the object to the result of subtracting one day (datetime.timedelta(days=1)) from the current time (timezone.now()), which is a timezone-aware datetime object representing the current date and time.

If the pub_date attribute is greater than or equal to the result of subtracting one day from the current time, then the method returns True, indicating that the object was published recently. Otherwise, it returns False.

It's important to note that the timezone.now() function is used to get the current date and time in the timezone of the Django project. This ensures that the comparison is accurate and takes into account any timezone differences.'''

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text