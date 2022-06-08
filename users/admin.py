
from django.contrib import admin
from .models import User


# @admin.register(User)
# class User(admin.ModelAdmin):
#     list_display = ('email', 'is_active', 'is_staff', 'is_superuser')
#     list_editable = ('is_active', 'is_staff', 'is_superuser')
admin.site.register(User)