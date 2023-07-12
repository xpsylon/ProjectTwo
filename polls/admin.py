from django.contrib import admin  
# Importing the admin module from Django

from .models import Choice, Question  
# Importing the Choice and Question models from the current directory


class ChoiceInline(admin.TabularInline):
    model = Choice  
    # Specifies the model to be used for the inline form (Choice model)
    extra = 1  
    # Specifies the number of extra forms to display for adding choices


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),  
        # Defines the fields to be displayed in the admin form for Question model
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),  
        # Additional field with collapsing class (from css django built in classes)
    ]
    inlines = [ChoiceInline]  
    # Specifies the inline form to be used for the Question model


admin.site.register(Question, QuestionAdmin)  
# Registers the Question model with the admin site using QuestionAdmin configuration

""" Certainly! Here's the code neatly organized with line-by-line explanations:

python

from django.contrib import admin  # Importing the admin module from Django

from .models import Choice, Question  # Importing the Choice and Question models from the current directory


class ChoiceInline(admin.StackedInline):
    model = Choice  # Specifies the model to be used for the inline form (Choice model)
    extra = 3  # Specifies the number of extra forms to display for adding choices


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),  # Defines the fields to be displayed in the admin form for Question model
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),  # Additional field with collapsing class
    ]
    inlines = [ChoiceInline]  # Specifies the inline form to be used for the Question model


admin.site.register(Question, QuestionAdmin)  # Registers the Question model with the admin site using QuestionAdmin configuration

Explanation:

    from django.contrib import admin: Imports the admin module from the Django framework, 
    which provides functionality for creating administration interfaces.

    from .models import Choice, Question: Imports the Choice and Question models from the current directory. 
    These models are assumed to be defined in a models.py file within the same directory.

    class ChoiceInline(admin.StackedInline): Defines a class ChoiceInline that inherits from admin.StackedInline. 
    This class represents an inline form for the Choice model within the admin interface.

    model = Choice: Specifies the model to be used for the inline form, which is the Choice model.

    extra = 3: Sets the number of extra forms to display for adding choices. 
    In this case, it will display three additional forms.

    class QuestionAdmin(admin.ModelAdmin): Defines a class QuestionAdmin that inherits from admin.ModelAdmin. 
    This class represents the configuration for the admin interface of the Question model.

    fieldsets = [...]: Defines a list of tuples representing the fieldsets for the admin form. 
    Each tuple contains a title and a dictionary specifying the fields to be displayed.

    (None, {"fields": ["question_text"]}):
    Represents the first fieldset. It has no title (None) and includes the "question_text" field.

    ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}): 
    Represents the second fieldset with the title "Date information". It includes the "pub_date" field and applies the "collapse" class to make it collapsible in the admin form.

    inlines = [ChoiceInline]: Specifies the inline form to be used for the Question model. 
    It assigns the ChoiceInline class to the inlines attribute of the QuestionAdmin class.

    admin.site.register(Question, QuestionAdmin): Registers the Question model with the admin site using the QuestionAdmin configuration.
    This makes the Question model accessible and editable through the admin interface. """