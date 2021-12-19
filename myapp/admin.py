from django.contrib import admin
from .models import User
# Register your models here.
@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'dob', 'gender', 'city', 'locality', 'pin', 'division','mobile', 'email', 'job_city', 'profile_image', 'my_file']