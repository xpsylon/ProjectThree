from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#By default Django Users dont have the option to upload a profile picture. So we'll create a Profiles model to add this functionality.
#It will have a ONE TO ONE relationship with the Users model. Always remember, a model is a table.

class Profile(models.Model):
    #creating a OneToOne relationship with User model. user (lowcase) is variable of Profile. CASCADE: if we delete User, we delete Profile. But not the 
    #other way around.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics') #name of directory where profile images will be saved.

    #dunder string for Profile output:
    def __str__(self) -> str:
        return f'{self.user.username} Profile'
        #output "eekemony Profile"

#After creating a new model (table), dont forget to run migrations.
#But with images, you'll first need to install Pillow.
#And register the model on admin page of the app.


