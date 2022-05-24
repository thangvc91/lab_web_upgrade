from django.contrib import admin

# Register your models here.
from .models import ClientUrl, Register1
admin.site.register(Register1)

admin.site.register(ClientUrl)