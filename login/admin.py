from django.contrib import admin
from .models import *
# Register your models here.

class login_home(admin.ModelAdmin):
	list_diaplay=["name","number"]
admin.site.register(login_data,login_home)
