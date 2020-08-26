from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class UserAdminCustom(UserAdmin):
   list_display = ('username','is_staff', 'is_superuser', 'is_active')
   list_filter = ('is_staff', 'is_superuser', 'is_active', 'username')
   list_editable = ('is_active','is_staff',)
   search_fields = ('username', )

admin.site.unregister(User)
admin.site.register(User, UserAdminCustom)