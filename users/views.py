from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def registro(request):
    form = UserCreationForm
    return render(request, 'users/register.html', {'formulario': form})