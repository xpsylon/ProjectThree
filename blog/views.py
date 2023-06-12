from django.shortcuts import render
from django.http import HttpResponse #dont need it, we are not using it

#dummy data in the beginning for the posts. list of dictionaries:
posts = [
    {
        'author': 'Jake La Motta',
        'title': 'Blog Post 1',
        'content': 'El knockout y yo',
        'date_posted': 'Junio 14, 1945'
    },
    {
        'author': 'Fatboy Slim',
        'title': 'Blog Post 2',
        'content': 'Boogie Woogie and Waltz',
        'date_posted': 'Diciembre 11, 1962'
    }


]

# Create your views here.
def home(request):
    #creamos un diccionario usando como valor la variable posts.
    context = {
        'posts': posts
    }
    #return HttpResponse('<h1>Blog Home</h1>')
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
