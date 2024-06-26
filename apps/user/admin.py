from django.contrib import admin

# Register your models here.

from django.contrib import admin

from apps.user.models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone_number', 'last_name', 'first_name', 'date_joined')
