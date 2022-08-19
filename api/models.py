from django.db import models

# Create your models here.

class FizzBuzz(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    user_agent = models.TextField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    

