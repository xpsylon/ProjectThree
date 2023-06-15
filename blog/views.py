from django.shortcuts import render
from django.http import HttpResponse #dont need it, we are not using it
from .models import Post

# Create your views here.
def home(request):
    #creamos un diccionario usando como valor la variable posts. En el html template se loopea por la clave y da como respuesta el valor. El valor es la lista
    #de diccionarios.
    context = {
        'cosas': Post.objects.all()
    }
    #return HttpResponse('<h1>Blog Home</h1>')
    return render(request, 'blog/home.html', context)

def about(request):
    #a este le agregamos el titulo como tercer argumento
    return render(request, 'blog/about.html', {'titulo': 'Cosas del Blog'})
