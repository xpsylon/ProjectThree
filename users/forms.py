#CREACION DE FORMULARIO DE USUARIO AGREGANDO CAMPO EMAIL Y METADATA.
from django import forms #para agregar el campo email faltante en UserCreationForms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    #https://docs.djangoproject.com/en/4.2/topics/db/models/#meta-options
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] #fields attribute is mandatory for ModelForms

#importamos la clase ModelForm de django.forms
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

'''Sure! Let's go through the code line by line:

1. `from django import forms`: This line imports the `forms` module from the `django` package. It is used to define and work with forms in Django.

2. `from django.contrib.auth.models import User`: This line imports the `User` model from the `django.contrib.auth.models` module. 
The `User` model is provided by Django and is used for user authentication and authorization.

3. `from django.contrib.auth.forms import UserCreationForm`: This line imports the `UserCreationForm` class from the `django.contrib.auth.forms` 
module. `UserCreationForm` is a pre-defined form in Django that provides a set of fields for creating a new user.

5. `class UserRegisterForm(UserCreationForm):`: This line defines a new class called `UserRegisterForm` that inherits from the `UserCreationForm` class.
 This means that `UserRegisterForm` will have all the fields and functionality provided by `UserCreationForm` and can also add or modify its behavior.

6. `email = forms.EmailField()`: This line defines a new field called `email` in the `UserRegisterForm` class using the `EmailField` class 
from the `forms` module. `EmailField` is a field type that validates input as an email address.

9. `class Meta:`: This line starts the definition of an inner class called `Meta` within the `UserRegisterForm` class. 
The `Meta` class is used to provide metadata or configuration options for the form.

10. `model = User`: This line sets the `model` attribute of the `Meta` class to the `User` model. 
It specifies that the form is associated with the `User` model, which means it will create or update instances of the `User` model when the form is submitted.

11. `fields = ['username', 'email', 'password1', 'password2']`: This line sets the `fields` attribute of the `Meta` class to a list of field names. 
It specifies which fields from the associated model should be included in the form. In this case, the form will include fields for `username`, `email`,
 `password1`, and `password2`.'''

