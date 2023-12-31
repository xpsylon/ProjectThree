from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse #for returning the absolute url as a string and not redirect it now. it will be redirected inside the view.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detalle-posteo', kwargs={'pk': self.pk})

"""
    A model representing a blog post.

    Attributes:
        title (CharField): The title of the blog post.
        content (TextField): The content of the blog post.
        date_posted (DateTimeField): The date and time when the blog post was created.
        author (ForeignKey): The author of the blog post, linked to the User model.

    Methods:
        __str__: Returns a string representation of the blog post.
    """
"""
        Returns a string representation of the blog post.

        Returns:
            str: The title of the blog post.
"""