from django.contrib import admin
from profiles_api import models

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['email','name']
    

admin.site.register(models.UserProfile,UserProfileAdmin)