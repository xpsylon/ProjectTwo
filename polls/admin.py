from django.contrib import admin
# para que se pueda editar desde el admin site.

from .models import Question

admin.site.register(Question)
