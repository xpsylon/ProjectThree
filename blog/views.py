from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm #para form en def form_valid
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse #dont need it, we are not using it
#ListView para ver lista de posteos, DetailView para ver cada posteo en detalle y CreateView para nuevos posteos.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
#Como el decorator @login_required para function based views, este es para class based views. 
#se pasa simplemente como argumento. Te manda al Login si al intentar crear un post nuevo no estas logeado.
#El UserPassesTestMixin es para que solo el autor pueda actualizar su post.

# Esta function view ha sido totalmente reemplazada por PostListView. Esta activa solo a efectos de enseñanza y comparacion. 
def home(request):
    #creamos un diccionario usando como valor la variable posts. En el html template se loopea por la clave y da como respuesta el valor. El valor es la lista
    #de diccionarios.
    context = {
         'cosas': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

#creating a class-based view (instead of function-based view) from ListView type:
#REEMPLAZA TOTALMENTE A LA FUNCTION VIEW HOME. El context home es reemplazado por context_object_name:
class PostListView(ListView):
    #todas estas variables son con nombres predefinidos por la clase madre ListView
    model = Post
    template_name = 'blog/home.html' #porque sino va por default a blog/post_list.html
    context_object_name = 'cosas' #porque sino por default las ListViews buscan loopear por object_list
    ordering = ['-date_posted'] #ordenar de fecha mas nueva a mas vieja (con el signo -).
    paginate_by = 5 #Paginator

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'cosas'
    # ordering = ['-date_posted'] will be overwritten by the get_queryset
    paginate_by = 5

    def get_queryset(self) -> QuerySet[Any]:
        user = get_object_or_404(User, username=self.kwargs.get('username')) #kwargs es un diccionario.
        return Post.objects.filter(author=user).order_by('-date_posted')

#creamos una lista de DetailView (posteos individuales), usando como nombres las convenciones de django. P.ej el template: <app>/<model>_<viewtype>.html
#entonces vamos a crear un template llamado post_detail.html en templates/blog
class PostDetailView(DetailView):
    model = Post

#Creamos clase-based view heredando de CreateView.
#Por default va al template blog/post_form.html
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    #pide el autor para crear post
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    #pide el autor para actualizar post
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)
    #chequea que sea el autor quien escribio el post.
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    #chequea que sea el autor que escribio el post para poder deletear:
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

''' The code defines a class named PostCreateView which inherits from the CreateView class. 
    CreateView is a generic view provided by Django for creating new objects.

    model = Post: This line sets the model attribute of the PostCreateView class to the Post model. 
    It indicates that the view is used for creating instances of the Post model.

    fields = ['title', 'content']: This line sets the fields attribute of the PostCreateView class to a list containing 
    the names of the fields that should be included in the form for creating a new Post object. In this case, the form will have fields for title and content.

    def form_valid(self, form: BaseModelForm) -> HttpResponse:: This line defines a method named form_valid within the PostCreateView class. 
    This method is responsible for handling the form submission when it is valid. It takes two parameters: self (referring to the instance of the class) 
    and form (referring to the form instance).

    form.instance.author = self.request.user: This line assigns the author field of the form.instance (the new Post object) 
    to the currently authenticated user (self.request.user). It associates the currently logged-in user as the author of the post.

    return super().form_valid(form): This line calls the form_valid method of the parent class (CreateView) using the super() function. 
    It passes the form as an argument to the parent's form_valid method. This allows the parent class to perform its default behavior 
    for form validation and object creation. Finally, it returns the result of the parent's form_valid method, which in this case is an HttpResponse object.

In summary, this code defines a class-based view (PostCreateView) that extends the CreateView class. 
It specifies the Post model as the model to create objects for and sets the title and content fields as the fields to be included in the form. 
When the form is submitted and valid, the form_valid method is called, which assigns the currently logged-in user as the author of the post and 
then calls the form_valid method of the parent class to handle the default behavior of object creation.'''

#FUNCTION-BASED VIEW PARA EL ABOUT THE BLOG
def about(request):
    #a este le agregamos el titulo como tercer argumento
    return render(request, 'blog/about.html', {'titulo': 'Cosas del Blog'})

#JUST A TEST VIEW FOR CHECKING THE BASE.HTML TEMPLATE:
def base(request):
    return render(request, 'blog/base.html')

def base2(request):
    return render(request, 'blog/base2.html')

