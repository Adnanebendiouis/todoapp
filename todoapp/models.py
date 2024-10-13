from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    username = models.CharField(max_length=50)
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    
class Tasks(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    
