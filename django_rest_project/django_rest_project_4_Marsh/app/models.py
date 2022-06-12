
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
class StaffUrl(models.Model):
    staffpass = models.CharField(max_length=20, null=False)
    staffname = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=200,null=False)
    clientname = models.CharField(max_length=200,null=True)
    staffurl =models.CharField(max_length=500,null=False)
    year =models.IntegerField(null=True)
    def __str__(self): return self.staffname
    
class Bat(models.Model):
    batpassword = models.CharField(max_length=20, null=False)
    batuser = models.CharField(max_length=50, null=False)
    batemail = models.CharField(max_length=50, null=False)
    batrelationship = models.CharField(max_length=50, null=True)
    batdob = models.CharField(max_length=50, null=True)
    batgender = models.CharField(max_length=10, null=True)
    batid = models.CharField(max_length=20, null=True)
    def __str__(self): return self.batemail