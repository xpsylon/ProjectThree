from django.contrib import admin
from .models import Post

admin.site.register(Post)

"""
Register the Post model with the admin site.
This code registers the Post model with the Django admin site, enabling it to be managed through the admin interface. By registering the model, you can perform CRUD operations (Create, Read, Update, Delete) on Post objects using the admin site.
Note: The admin.site.register() method is used to register a model with the admin site. Once registered, the model's data can be viewed, edited, and deleted through the admin interface.

Example usage:
    admin.site.register(Post)

"""


