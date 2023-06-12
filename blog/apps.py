from django.apps import AppConfig

#BlogConfig es child de la clase AppConfig, que es una built-in clase de Django.
class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
