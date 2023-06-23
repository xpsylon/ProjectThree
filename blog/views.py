from django.shortcuts import render
#from django.http import HttpResponse #dont need it, we are not using it
from django.views.generic import ListView #for ListView type of class based view.
from .models import Post

# Create your views here.
def home(request):
    #creamos un diccionario usando como valor la variable posts. En el html template se loopea por la clave y da como respuesta el valor. El valor es la lista
    #de diccionarios.
    context = {
         'cosas': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

#creating a class-based view (instead of function-based view) from ListView type:
class PostListView(ListView):
    #todas estas variables son con nombres predefinidos por la clase madre ListView
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'cosas' #porque sino por default las ListViews buscan loopear por object_list
    ordering = ['-date_posted'] #ordebar de fecha mas nueva a mas vieja (con el signo -)

def about(request):
    #a este le agregamos el titulo como tercer argumento
    return render(request, 'blog/about.html', {'titulo': 'Cosas del Blog'})
