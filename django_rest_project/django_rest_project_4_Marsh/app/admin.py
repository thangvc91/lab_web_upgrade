from django.contrib import admin
from import_export.admin import ExportActionMixin
# Register your models here.
from .models import Bat, ClientUrl, Register1, StaffUrl
# admin.site.register(Register1)

admin.site.register(ClientUrl)
# admin.site.register(StaffUrl)

class Register1Admin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('phone', 'name', 'email')
class StaffAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('staffpass','staffname','clientname','description','staffurl','year')
admin.site.register(Register1,Register1Admin)
admin.site.register(StaffUrl,StaffAdmin)


admin.site.register(Bat)