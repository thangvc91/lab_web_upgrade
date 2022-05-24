
from django.db import models

# Create your models here.
# from django.db import models
    
class Register1(models.Model):
    phone = models.CharField(max_length=20, unique=False, null=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True)

    def __str__(self): return self.name
class ClientUrl(models.Model):
    clientpass = models.CharField(max_length=50,null=False)
    clientname = models.CharField(max_length=100,null=False)
    description = models.CharField(max_length=100,null=False)
    clienturl =models.CharField(max_length=500,null=False)
    def __str__(self): return self.clientname