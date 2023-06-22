from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required #built in django decorator for profile view.

def registro(request):
    #This line defines a function called registro. The request parameter is a standard Django request object 
    # that contains information about the current request, such as the user's IP address, the browser they are using, and the URL they are visiting.
    if request.method == 'POST':
    #This line checks to see if the request method is POST. If it is, then the user has submitted the registration form.
        form = UserRegisterForm(request.POST)
    #This line creates a new UserRegisterForm instance and populates it with the data that the user submitted in the registration form.
        if form.is_valid():
            #Guarda el usuario en la base de datos:#
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Cuenta creada para {username}. Ya puede iniciar sesion.')
            return redirect('entrar') #redirige a login una vez que el formulario se envio correctamente.
    else:
        form = UserRegisterForm() 
    #This line is executed if the request method is not POST. In this case, the user has not yet submitted the registration form, 
    #so we need to create a new, empty UserRegisterForm instance.

    return render(request, 'users/register.html', {'formulario': form})
    #This line renders the users/register.html template, passing it the form object as an argument. 
    #The users/register.html template will then display the registration form to the user.

    #CHECK https://docs.djangoproject.com/en/4.2/topics/forms/

#VIEW FOR PROFILE (with login_required decorator)
@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
        
        if user_form.is_valid and profile_form.is_valid:
            user_form.save()
            profile_form.save()

            messages.success(request, f'Datos correctamente actualizados')
            return redirect('perfil')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'form_usuario': user_form,
        'form_perfil': profile_form
    }
    return render(request, 'users/profile.html', context)

'''The @login_required decorator indicates that the user must be logged in to access the profile view function. 
It adds a layer of authentication to ensure that only authenticated users can view their profile.

The profile function takes a request parameter, which represents the HTTP request made by the user. It is an instance of the HttpRequest class and 
contains information about the user's request.

Inside the function, two form objects, UserUpdateForm and ProfileUpdateForm, are created. These forms are likely used for updating user and profile information on the profile page.

A context dictionary is created to pass data to the template rendering engine. It contains two keys, 'form_usuario' and 'form_perfil', 
which are associated with the user_form and profile_form objects, respectively.

Finally, the function returns a rendered HTML response using the render function. It renders the 'users/profile.html' template with the provided context dictionary, 
displaying the user profile page.'''