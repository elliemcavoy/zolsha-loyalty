from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'email', 'phone_number',
                    'birthday')




admin.site.register(UserProfile)
