from django.apps import AppConfig
#automatico cuando se instala una app. Ahora hay que registrarla en INSTALLED_APPS


class PollsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'
