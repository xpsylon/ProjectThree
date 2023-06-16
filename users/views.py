from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def registro(request):
    #This line defines a function called registro. The request parameter is a standard Django request object 
    # that contains information about the current request, such as the user's IP address, the browser they are using, and the URL they are visiting.
    if request.method == 'POST':
    #This line checks to see if the request method is POST. If it is, then the user has submitted the registration form.
        form = UserCreationForm(request.POST)
    #This line creates a new UserCreationForm instance and populates it with the data that the user submitted in the registration form.
        if form.is_valid:
            username = form.cleaned_data.get('username')
    else:
        form = UserCreationForm()
    #This line is executed if the request method is not POST. In this case, the user has not yet submitted the registration form, 
    #so we need to create a new, empty UserCreationForm instance.

    return render(request, 'users/register.html', {'formulario': form})
    #This line renders the users/register.html template, passing it the form object as an argument. 
    #The users/register.html template will then display the registration form to the user.