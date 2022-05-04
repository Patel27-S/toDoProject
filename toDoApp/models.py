from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    pass



class toDoTable(models.Model):
    content_maker = models.ForeignKey(
                    'CustomUser',
                    on_delete=models.CASCADE)
    content = models.TextField()
