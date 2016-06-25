from django.contrib import admin
from c_growth.models import Run, Data

# Register your models here.

class DataAdmin(admin.ModelAdmin):
    list_display = ['name','run','principle','rate','year','total']

class RunAdmin(admin.ModelAdmin):
    list_display = ['name','description','date']

admin.site.register(Data, DataAdmin)
admin.site.register(Run, RunAdmin)
