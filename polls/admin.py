from django.contrib import admin
# para que se pueda editar desde el admin site.
from .models import Question, Choice

#cambia el orden de pub_date (1) y question_text (2):
class QuestionAdmin(admin.ModelAdmin):
    #agregamos el field set conformado por una lista que contiene dos tuplas que cada una contiene un diccionario cuyo valor es una lista.
    fieldsets = [
        (None, {'fields': ['question_text']}), 
        ('Date information', {'fields': ['pub_date']})
    ]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

""" Certainly! Here's a breakdown and explanation of each line of code:

1. `from django.contrib import admin`: This line imports the `admin` module from the `django.contrib` package. 
 It allows us to access and customize the Django administration site.

2. `from .models import Question`: This line imports the `Question` model from the local module's `models.py` file. 
 The dot (`.`) indicates that the `models.py` file is in the same directory as the current file.

3. `class QuestionAdmin(admin.ModelAdmin):`: This line defines a new class named `QuestionAdmin` which inherits from `admin.ModelAdmin` class. 
 This class will be used to customize the admin interface for the `Question` model.

4. `fieldsets = [...]`: This line defines the `fieldsets` attribute of the `QuestionAdmin` class. 
 It is a list that specifies how the form fields should be grouped and displayed in the admin interface. Each element of the list is a tuple that contains a label for the fieldset and a dictionary that defines the fields to be included in that fieldset.

5. `(None, {"fields": ["question_text"]}),`: This line defines the first fieldset element. 
 It consists of a tuple with `None` as the label and a dictionary with a single key-value pair. The key `"fields"` represents the fields to be included in the fieldset, and the value `["question_text"]` specifies that only the field `"question_text"` should be included.

6. `("Date information", {"fields": ["pub_date"]}),`: This line defines the second fieldset element. 
 It follows the same structure as the previous line but includes the `"pub_date"` field in a fieldset labeled `"Date information"`.

7. `admin.site.register(Question, QuestionAdmin)`: This line registers the `Question` model with the `QuestionAdmin` class in the Django admin site. 
 It makes the `Question` model visible and editable in the admin interface, using the customizations defined in `QuestionAdmin`.

These lines of code demonstrate how to import the necessary modules, define a custom admin class, specify fieldsets for grouping form fields, 
 and register the model with the admin site. This allows you to have more control over the appearance and behavior of the `Question` model in the Django administration site. """