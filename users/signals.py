#THIS IS FOR AUTOMATICALLY CREATE A PROFILE WHEN A USER REGISTERS.
'''The signals.py file in Django is used to define and manage signals. Signals are a way for 
different parts of a Django application to communicate with each other and perform certain actions when specific events occur.

In simpler terms, signals allow you to define certain triggers or events in your Django application that can be 
detected by other parts of the application. When a specific event happens, such as a new object being saved in the database 
or a user logging in, a signal is sent out. Other parts of the application can listen for these signals and take some action in response.

The signals.py file is where you define these signals and the actions that should be taken when they occur. It acts as a central place
for managing and organizing these signals. Typically, you will create a signal by subclassing the `django.dispatch.Signal` class 
and then define the specific actions to be taken in response to that signal.

For example, let's say you have a Django application for a blog. In your signals.py file, you could define a signal called `post_created`, 
which gets triggered whenever a new blog post is created. You can then define a function to handle this signal, such as sending 
an email notification to the blog author or updating some related data.

By using signals, you can decouple different parts of your application, making them more modular and easier to maintain. 
It allows you to define certain events and actions in a flexible and extensible way, without directly coupling different components together.

Overall, the signals.py file in Django helps you define and manage signals, which are a way for different parts of 
your application to communicate and perform actions when specific events occur. It promotes loose coupling and modular design,
making your code more flexible and maintainable.

https://docs.djangoproject.com/en/4.2/ref/signals/
'''

from django.db.models.signals import post_save #action triggered after saving an user
from django.contrib.auth.models import User #the sender
from django.dispatch import receiver #decorator 
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()