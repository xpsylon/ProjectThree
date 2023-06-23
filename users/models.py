from django.db import models
from django.contrib.auth.models import User
from PIL import Image
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
    
    def save(self):
        super().save() #we put the save method of the parent class
        #one method for resizing images:
        imagen = Image.open(self.image.path)
        if imagen.height > 300 or imagen.width > 300:
            peso_max = (300, 300) #tupla
            imagen.thumbnail(peso_max) #thumbnail metodo de PIL
            imagen.save(self.image.path)


#After creating a new model (table), dont forget to run migrations.
#But with images, you'll first need to install Pillow.
#And register the model on admin page of the app.


