from django.contrib import admin
from import_export.admin import ExportActionMixin
# Register your models here.
from .models import ClientUrl, Register1
# admin.site.register(Register1)

admin.site.register(ClientUrl)


class Register1Admin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('phone', 'name', 'email')

admin.site.register(Register1,Register1Admin)