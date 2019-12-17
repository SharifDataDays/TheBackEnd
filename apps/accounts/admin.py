from django.contrib.auth.models import User

from apps.accounts.models import UserProfile
from django.contrib import admin

# Register your models here


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'email', 'first_name', 'last_name', 'birth_date', 'residence', 'education']
